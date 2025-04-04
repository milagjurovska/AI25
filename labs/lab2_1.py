import math

from searching_framework import Problem, astar_search

class House(Problem):
    def __init__(self, start, dozvoleni):
        super().__init__(start)
        self.dozvoleni = dozvoleni
        self.grid=(5,9)

    def valid(self, position, new_house):
        x,y = position
        if not (0 <= x < self.grid[0] and 0 <= y < self.grid[1]):
            return False
        if y == 8:
            return position == new_house
        if (x, y) not in self.dozvoleni:
            return False

        return True

    def move_kukja(self, kukja, pozicija):
        x, y = kukja
        if pozicija == "desno":
            if x+1<self.grid[0]:
                return (x + 1, y), pozicija
            else:
                pozicija = "levo"
                return (x - 1, y), pozicija
        else:
            if x-1>=0:
                return (x - 1, y), pozicija
            else:
                pozicija = "desno"
                return (x + 1, y), pozicija

    def successor(self, state):
        successors = dict()
        manx, many = state[0]
        kukja = state[1]

        nova=self.move_kukja(kukja, state[2])
        new_kukja = nova[0]
        poz=nova[1]
        successors["Stoj"] = ((manx, many), new_kukja, poz)


        new_y = many + 1
        if self.valid((manx,new_y), new_kukja):
            successors["Gore 1"] = ((manx, new_y), new_kukja, poz)

        new_y=many+2
        if self.valid((manx,new_y), new_kukja):
            successors["Gore 2"] = ((manx, new_y), new_kukja, poz)

        new_x=manx+1
        new_y=many+1
        if self.valid((new_x, new_y), new_kukja):
            successors["Gore-desno 1"] =((new_x, new_y), new_kukja, poz)

        new_x=manx+2
        new_y= many+2
        if self.valid((new_x, new_y), new_kukja):
            successors["Gore-desno 2"] = ((new_x, new_y), new_kukja, poz)

        new_x = manx - 1
        new_y= many + 1
        if self.valid((new_x, new_y), new_kukja):
            successors["Gore-levo 1"] = ((new_x, new_y), new_kukja, poz)

        new_x = manx - 2
        new_y= many + 2
        if self.valid((new_x, new_y), new_kukja):
            successors["Gore-levo 2"] = ((new_x, new_y), new_kukja, poz)

        return successors

    def actions(self, state):
        return self.successor(state).keys()
    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):
        state=node.state
        man=state[0]
        kukja = state[1]
        return math.sqrt((man[0] - kukja[0]) ** 2 + (man[1] - kukja[1]) ** 2) / 5

    def goal_test(self, state):
        man, kukja = state[0], state[1]
        return man==kukja


if __name__ == '__main__':
    allowed = [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (0, 2), (2, 2), (4, 2), (1, 3), (3, 3), (4, 3), (0, 4), (2, 4),
               (2, 5), (3, 5), (0, 6), (2, 6), (1, 7), (3, 7)]

    line1=input().split(",")
    line2=input().split(",")
    line3=input().strip()
    choveche=(int(line1[0]), int(line1[1]))
    kukja=(int(line2[0]), int(line2[1]))

    house=House((choveche, kukja, line3), allowed)
    result = astar_search(house)
    if result is not None:
        print(result.solution())
    else:
        print("No solution")

from searching_framework import Problem, astar_search

class Labyrinth(Problem):
    def __init__(self, start, goal, obstacles, grid):
        super().__init__(start, goal)
        self.obstacles = obstacles
        self.grid = grid

    def successor(self, state):
        successors = dict()
        man=state

        new_man=man[0]+2, man[1]
        if self.valid(new_man) and (new_man[0]-1,new_man[1]) not in self.obstacles:
            successors["Desno 2"] = new_man

        new_man = man[0] + 3, man[1]
        if self.valid(new_man)and (new_man[0]-1,new_man[1]) not in self.obstacles and (new_man[0]-2,new_man[1]) not in self.obstacles:
            successors["Desno 3"] = new_man

        new_man = man[0], man[1]+1
        if self.valid(new_man):
            successors["Gore"] = new_man

        new_man = man[0], man[1]-1
        if self.valid(new_man):
            successors["Dolu"] = new_man

        new_man = man[0] - 1, man[1]
        if self.valid(new_man):
            successors["Levo"] = new_man

        return successors

    def valid(self, state):
        x,y=state
        if (x,y) in self.obstacles:
            return False
        if not (0<=x<self.grid and 0<=y<self.grid):
            return False
        return True

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):
        state=node.state
        goal=self.goal
        return (abs(state[0]-goal[0]) + abs(state[1]-goal[1]))/5

if __name__ == '__main__':
    N=int(input())
    walls=int(input())
    walls_list=[]
    for i in range(walls):
        line = input().split(",")
        walls_list.append((int(line[0]),int(line[1])))

    line2=input().split(",")
    line3=input().split(",")

    choveche=(int(line2[0]), int(line2[1]))
    kukja=(int(line3[0]), int(line3[1]))

    labyrinth=Labyrinth(choveche, kukja, walls_list, N)
    result=astar_search(labyrinth)
    if result is not None:
        print(result.solution())
    else:
        print("No solution")

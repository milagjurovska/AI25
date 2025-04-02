from searching_framework import Problem, breadth_first_graph_search


nasoki = {
    "Up": (0, -1),
    "Right": (1, 0),
    "Down": (0, 1),
    "Left": (-1, 0)
}


def change_direction(current, move):
    directions = ["Up", "Right", "Down", "Left"]
    index = directions.index(current)

    if move == "SvrtiLevo":
        return directions[(index + 1) % 4]
    elif move == "SvrtiDesno":
        return directions[(index - 1) % 4]
    return current


class Snake(Problem):
    def __init__(self, initial, obstacles, goal=None):
        super().__init__(initial, goal)
        self.grid_size = 10
        self.obstacles = obstacles

    def successor(self, state):
        successors = dict()
        head, body, direction, apples = state

        dvizhenja = ["ProdolzhiPravo", "SvrtiDesno", "SvrtiLevo"]

        for move in dvizhenja:
            new_dir = change_direction(direction, move)
            new_head = (head[0] + nasoki[new_dir][0], head[1] + nasoki[new_dir][1])

            if self.valid_move(new_head, body):
                new_body = list(body)
                new_body.insert(0, head)

                new_apples = set(apples)
                if new_head in new_apples:
                    new_apples.remove(new_head)
                else:
                    new_body.pop()

                successors[move] = (new_head, tuple(new_body), new_dir, tuple(new_apples))

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[3]) == 0

    def valid_move(self, new_head, body):
        x, y = new_head
        if x < 0 or x >= self.grid_size or y < 0 or y >= self.grid_size:
            return False
        if (x, y) in self.obstacles:
            return False
        if (x, y) in body[:-1]:
            return False
        return True


if __name__ == '__main__':
    start_tail = ((0, 8), (0, 9))
    start_head = (0, 7)

    N = int(input())
    greenlist = []
    for i in range(N):
        zeleni = input().split(',')
        greenlist.append((int(zeleni[0]), int(zeleni[1])))

    M = int(input())
    redlist = []
    for i in range(M):
        crveni = input().split(',')
        redlist.append((int(crveni[0]), int(crveni[1])))

    snake = Snake((start_head, start_tail, "Up", tuple(greenlist)), tuple(redlist), None)

    game = breadth_first_graph_search(snake)
    if game is not None:
        print(game.solution())
    else:
        print('No solution')

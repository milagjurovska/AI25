from searching_framework import *


# vtora grupa: dolu i levo, se sobiraat topkite

class Person(Problem):
    def __init__(self, initial, grid, boxes, goal=None):
        super().__init__(initial, goal)
        self.grid = grid
        self.boxes = boxes

    def goal_test(self, state):
        filled_bozes = state[1]
        return filled_bozes == self.boxes

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state).get(action)

    def successor(self, state):
        successors = dict()
        x, y = state[0]
        filled_bozes = state[1]
        remaining_balls = state[2]

        # Gore
        new_x, new_y = x, y + 1
        if new_y < self.grid and (new_x, new_y) not in self.boxes:
            new_filled_boxes = list(filled_bozes)
            new_remaining = remaining_balls
            for box in self.boxes:
                if box not in new_filled_boxes and max(abs(new_x - box[0]), abs(new_y - box[
                    1])) == 1 and new_remaining > 0:  # za proverka dali e sosed na kutija
                    new_filled_boxes.append(box)
                    new_remaining -= 1
            successors["Dvizhenje gore"] = ((new_x, new_y), tuple(new_filled_boxes), new_remaining)

        # Desno
        new_x, new_y = x + 1, y
        if new_x < self.grid and (new_x, new_y) not in self.boxes:
            new_filled_boxes = list(filled_bozes)
            new_remaining = remaining_balls
            for box in self.boxes:
                if box not in new_filled_boxes and max(abs(new_x - box[0]), abs(new_y - box[
                    1])) == 1 and new_remaining > 0:  # za proverka dali e sosed na kutija
                    new_filled_boxes.append(box)
                    new_remaining -= 1
            successors["Dvizhenje desno"] = ((new_x, new_y), tuple(new_filled_boxes), new_remaining)

        return successors
    # evristika za informirano: Chebyshev distance -  max(|x1-x2|, |y1-y2|)


if __name__ == '__main__':
    n = int(input())
    man_pos = (0, 0)
    m = int(input())
    kutii = []
    for i in range(n):
        line = input().split(",")
        kutii.append((int(line[0]), int(line[1])))

    person = Person((man_pos, (), m), n, tuple(kutii), None)
    print(breadth_first_graph_search(person))

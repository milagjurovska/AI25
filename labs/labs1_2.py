from searching_framework import Problem, breadth_first_graph_search

gol=[(7,2),(7,3)]
ball_impossible=[(2,2),(3,2),(4,2),(5,3),(6,3),(2,3),(4,3),(2,4),(3,4),(4,4),(6,4),(4,5),(5,5),(6,5)]

class Football(Problem):
    def __init__(self, attacker, ball):
        super().__init__((attacker, ball))
        self.gridsize=(8,6)
        self.obstacles=[(3,3),(5,4)]

    def successor(self, state):
        successors=dict()

        dvizhenja1=["Pomesti coveche gore", "Pomesti coveche dolu","Pomesti coveche desno", "Pomesti coveche gore-desno","Pomesti coveche dolu-desno"]
        dvizhenja2=["Turni topka gore","Turni topka dolu","Turni topka desno","Turni topka gore-desno","Turni topka dolu-desno"]

        for dv1 in dvizhenja1:
            new_attacker=self.move_attacker(state, dv1)
            if new_attacker is not None:
                new_state = (new_attacker, state[1])
                successors[dv1] = new_state

        for dv2 in dvizhenja2:
            new_ball=self.move_ball(state, dv2)
            if new_ball is not None:
                successors[dv2] = new_ball

        return successors

    def move_ball(self, state, action):
        ballx, bally = state[1]
        attackerx, attackery = state[0]

        new_manx, new_many = ballx, bally

        if action == "Turni topka gore" and  bally == attackery+1 and ballx == attackerx:
            bally+=1
        elif action == "Turni topka dolu" and bally==attackery-1 and ballx == attackerx:
            bally-=1
        elif action == "Turni topka desno" and ballx == attackerx+1 and bally == attackery:
            ballx+=1
        elif action == "Turni topka gore-desno" and ballx == attackerx+1 and bally == attackery+1:
            ballx+=1
            bally+=1
        elif action == "Turni topka dolu-desno" and ballx == attackerx+1 and bally == attackery -1:
            ballx+=1
            bally-=1
        else:
            return None

        new_ball = (ballx, bally)

        if new_ball in self.obstacles:
            return None
        if new_ball in ball_impossible:
            return None
        if not 0<=ballx<self.gridsize[0] or not 0<=bally<self.gridsize[1]:
            return None
        if new_ball ==(attackerx, attackery):
            return None


        new_attacker=(new_manx, new_many)
        if new_attacker in self.obstacles or new_attacker == new_ball:
            return None
        if not (0 <= new_attacker[0] < self.gridsize[0] or 0 <=new_attacker[1] < self.gridsize[1]):
            return None

        return new_attacker,new_ball

    def move_attacker(self, state, action):
        manx, many = state[0]

        if action == "Pomesti coveche gore":
            many+=1
        elif action == "Pomesti coveche dolu":
            many-=1
        elif action == "Pomesti coveche desno":
            manx+=1
        elif action == "Pomesti coveche dolu-desno":
            manx+=1
            many-=1
        elif action == "Pomesti coveche gore-desno":
            manx+=1
            many+=1

        else:
            return None

        if (manx,many) == state[1]:
            return None
        if (manx,many) in self.obstacles:
            return None
        if not 0<=manx<self.gridsize[0] or not 0<=many<self.gridsize[1]:
            return None

        return manx, many


    def actions(self, state):
        return self.successor(state).keys()
    def result(self, state, action):
        return self.successor(state)[action]
    def goal_test(self, state):
        return state[1] in gol

if __name__ == '__main__':
    line1=input().split(",")
    line2=input().split(",")
    napagjach=(int(line1[0]), int(line1[1]))
    topka=(int(line2[0]), int(line2[1]))

    football=Football(napagjach,topka)

    game=breadth_first_graph_search(football)
    if game is not None:
        print(game.solution())
    else:
        print("No Solution!")

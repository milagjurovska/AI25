from constraint import *


def send_money(S, E ,N, D, M, O, R, Y):
    send = S * 1000 + E * 100 + N * 10 + D
    more = M * 1000 + O * 100 + R * 10 + E
    money = M * 10000 + O * 1000 + N * 100 + E * 10 + Y
    return send + more == money


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = ["S", "E", "N", "D", "M", "O", "R", "Y"]
    for variable in variables:
        problem.addVariable(variable, Domain(set(range(10))))

    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(AllDifferentConstraint())



    problem.addConstraint(send_money, variables)

    # ----------------------------------------------------

    print(problem.getSolution())

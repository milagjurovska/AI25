from constraint import *

def machine(*args):
    predavanja=args[:1]
    vezhbi=args[-1]
    for p in predavanja:
        if p.split("_")[1] == vezhbi.split("_")[1]:
            return False
    return True

def timeslots(t1, t2):
    d1, v1 = t1.split("_")
    d2, v2 = t2.split("_")
    if d1 == d2 and abs(int(v1)-int(v2)) <= 1:
        return False
    return True


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    casovi_AI = input()
    casovi_ML = input()
    casovi_R = input()
    casovi_BI = input()

    AI_predavanja_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_predavanja_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
    R_predavanja_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14", "Mon_15", "Wed_10", "Wed_11", "Wed_12",
                           "Wed_13", "Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12", "Fri_13", "Fri_14", "Fri_15"]
    BI_predavanja_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]

    AI_vezbi_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_vezbi_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    BI_vezbi_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]

    # ---Tuka dodadete gi promenlivite--------------------
    ai_vars=[]
    ml_vars=[]
    bi_vars=[]
    r_vars=[]
    for i in range(int(casovi_AI)):
        problem.addVariable(f"AI_cas_{i+1}", AI_predavanja_domain)
        ai_vars.append(f"AI_cas_{i+1}")
    for i in range(int(casovi_ML)):
        problem.addVariable(f"ML_cas_{i+1}", ML_predavanja_domain)
        ml_vars.append(f"ML_cas_{i+1}")
    for i in range(int(casovi_R)):
        problem.addVariable(f"R_cas_{i+1}", R_predavanja_domain)
        r_vars.append(f"R_cas_{i+1}")
    for i in range(int(casovi_BI)):
        problem.addVariable(f"BI_cas_{i+1}", BI_predavanja_domain)
        bi_vars.append(f"BI_cas_{i+1}")

    problem.addVariable("AI_vezbi", AI_vezbi_domain)
    problem.addVariable("ML_vezbi", ML_vezbi_domain)
    problem.addVariable("BI_vezbi", BI_vezbi_domain)
    # ---Tuka dodadete gi ogranichuvanjata----------------
    variables=ai_vars + ml_vars + bi_vars + r_vars + ["AI_vezbi", "ML_vezbi", "BI_vezbi"]

    for i in variables:
        for j in variables:
            if i == j:
                continue
            problem.addConstraint(timeslots, (i,j ))
    problem.addConstraint(machine,  ml_vars + ["ML_vezbi"])

    # ----------------------------------------------------
    solution = problem.getSolution()

    print(solution)

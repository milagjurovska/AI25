from constraint import *

def timeslots(*variables):
    timeslots = set(variables)
    for timeslot in timeslots:
        if variables.count(timeslot)>4:
            return False
    return True

if __name__ == '__main__':
    num = int(input())

    papers = dict()

    paper_info = input()
    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        papers[title] = topic
        paper_info = input()

    # Tuka definirajte gi promenlivite
    variables = [v for v in papers.keys()]
    vae_ai = [v for v, a in papers.items() if a == "AI"]
    vae_ml = [v for v, m in papers.items() if m == "ML"]
    vae_nlp = [v for v, n in papers.items() if n == "NLP"]


    domain = [f'T{i + 1}' for i in range(num)]

    problem = Problem(BacktrackingSolver())

    # Dokolku vi e potrebno moze da go promenite delot za dodavanje na promenlivite
    problem.addVariables(variables, domain)

    # Tuka dodadete gi ogranichuvanjata

    problem.addConstraint(timeslots, variables)

    if 4>=len(vae_ai)>0:
        problem.addConstraint(AllEqualConstraint(), vae_ai)
    if 4>=len(vae_ml)>0:
        problem.addConstraint(AllEqualConstraint(), vae_ml)
    if 4>=len(vae_nlp)>0:
        problem.addConstraint(AllEqualConstraint(), vae_nlp)


    result = problem.getSolution()

    # Tuka dodadete go kodot za pechatenje

    for r in variables:
        print(f"{r} ({papers[r]}): {result[r]}")

from constraint import *

#od zadachi za vezhbanje: 4 trudovi vo termin, ako vkupen br e <= 4 site vo ist

def papers_per_timeslot(*papers):
    timeslots=set(papers)
    for ts in timeslots:
        if papers.count(ts) > 4:
            return False
    return True

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    #chitanje od input
    num=int(input())
    papers = dict()
    paper_info=input()
    while paper_info != 'end':
        title,topic=paper_info.split(' ')
        papers[title]=topic
        paper_info=input()


    varibales=[k for k in papers.keys()]
    variables_ai=[k for k, v in papers.items() if v == 'AI']
    variables_ml=[k for k, v in papers.items() if v == 'ML']
    variables_nlp=[k for k, v in papers.items() if v == 'NLP']

    domain=[f'T{i+1}' for i in range(num)]
    problem.addVariables(varibales, domain)
    problem.addConstraint(papers_per_timeslot, varibales)

    if 4>=len(variables_ai)>0:
        problem.addConstraint(AllEqualConstraint(), variables_ai)

    if 4>=len(variables_ml)>0:
        problem.addConstraint(AllEqualConstraint(), variables_ml)

    if 4>=len(variables_nlp)>0:
        problem.addConstraint(AllEqualConstraint(), variables_nlp)

    result= problem.getSolution()

    for paper in varibales:
        topic = papers[paper]
        timeslot=result[paper]
        print(f'{paper} ({topic}): {timeslot}')

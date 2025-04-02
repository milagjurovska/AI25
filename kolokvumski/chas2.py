from constraint import*

# na edno drvo eden shator, hor ili ver dozvoleno za shator, ne smee da se dopiraat shatori

def not_adjascent(tree1, tree2):
    return max(abs(tree1[0] - tree2[0]),abs(tree1[1] - tree2[1]))>1

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    n = int(input())
    drva = []
    for i in range(n):
        line = input().split(" ")
        drva.append((int(line[0]), int(line[1])))  # tree=tuple([int(e) for e in input().split(" ")]) drva.append(tree)

    dirs=[(0,1), (0,-1), (1,0), (-1,0)]

    for tree in drva:
        x,y = tree
        domain=[]
        for dx, dy in dirs:
            if 0<=x+dx<6 and  0<y+dy<6 and (x+dx, y+dy) not in drva:
                domain.append((x+dx, y+dy))
        problem.addVariable(tree, domain)

    problem.addConstraint(AllDifferentConstraint(), drva)
    for tree1 in drva:
        for tree2 in drva:
            if tree1 != tree2:
                problem.addConstraint(not_adjascent,(tree1, tree2))

    #vtora grupa: odreden br shatori koi se chitaat od standarden vlez
    ''' 
    cols vo input
    def count_in_col_i(*trees):      ///ova za bilo kolku argumenti
        for i in range(6):
            tents_in_col=0
            for tent in trees:
                if tent[0] == i:
                    tents_in_col+=1
            if tents_in_col!=cols[i]:
                return False
        return True
                
    problem.addConstraint(count_in_col_i, drva)
    '''

    solution = problem.getSolution()
    for tree in drva:
        print(solution[tree][0], solution[tree][1])


'''
input:
6
2 1
4 1 
5 0
3 2
2 4
2 3
'''

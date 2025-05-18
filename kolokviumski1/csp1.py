from constraint import *

def sostanok(vreme, simona, marija, petar):
    marija_pris = [14, 15, 18]
    simona_pris=[13, 14,16,19]
    petar_pris=[12,13,16,17,18,19]
    if vreme not in simona_pris or simona == 0:
        return False
    if vreme not in marija_pris and marija == 1:
        return False
    if vreme not in petar_pris and petar == 1:
        return False
    return petar + marija >= 1 and simona == 1

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ---Dadeni se promenlivite, dodadete gi domenite-----
    problem.addVariable("Marija_prisustvo", [0,1])
    problem.addVariable("Simona_prisustvo", [0,1])
    problem.addVariable("Petar_prisustvo", [0,1])
    problem.addVariable("vreme_sostanok", [12,13,14,15,16,17,18,19])
    # ----------------------------------------------------

    # ---Tuka dodadete gi ogranichuvanjata----------------

    problem.addConstraint(sostanok, ("vreme_sostanok","Simona_prisustvo", "Marija_prisustvo", "Petar_prisustvo"))
    # ----------------------------------------------------
    solutions=problem.getSolutions()
    for solution in solutions:
        print({'Simona_prisustvo': solution['Simona_prisustvo'], 'Marija_prisustvo': solution['Marija_prisustvo'], 'Petar_prisustvo': solution['Petar_prisustvo'], 'vreme_sostanok': solution['vreme_sostanok']})

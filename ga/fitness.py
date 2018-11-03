from models.individual import Individual
from models.constraints.constraint import Constraint

def calc_fitness(indiv: Individual, *constraints: Constraint) -> int:
    for event in indiv.schedule:
        for constraint in constraints:
            constraint.each_event(event)
    for constraint in constraints:
        indiv.fitness += constraint.get_final_fitness()
    return indiv.fitness

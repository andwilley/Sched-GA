from models.individual import Individual
from models.constraints.constraint import Constraint

def calc_fitness(indiv: Individual, *constraints: Constraint) -> int:
    # for each event, based on event
    #   check pilot conflict
    #   check pilot crew day
    #   update the pilot start and end time
    #   
    return 0

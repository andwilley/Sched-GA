from typing import List
from app.models.individual import Individual
from app.models.state import State
from app.models.constraints.constraint import Constraint
from app.models.constraints.crew_day import CrewDay
from app.models.constraints.no_event_overlap import NoEventOverlap

def calc_fitness(indiv: Individual, *constraints: Constraint) -> int:
    fitness = 0
    for event in indiv.schedule:
        for constraint in constraints:
            constraint.each_event(event)
    for constraint in constraints:
        fitness += constraint.get_final_fitness()
    return fitness

def get_constraints(state: State) -> List[Constraint]:
    return [CrewDay(state), NoEventOverlap(state)]

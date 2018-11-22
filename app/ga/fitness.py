from typing import List
import math
from app.models.individual import Individual
from app.models.state import State
from app.models.constraints.constraint import Constraint
from app.models.constraints.crew_day import CrewDay
from app.models.constraints.no_event_overlap import NoEventOverlap
from app.models.constraints.fair_work_hours import FairWorkHours
from app.models.constraints.undesirable_shifts import UndesirableShifts
from app.models.constraints.last_odo import LastODO

def calc_fitness(indiv: Individual, *constraints: Constraint) -> float:
    # mutates indiv (is_feasible)
    fitness = 0.0
    for event in indiv.schedule:
        for constraint in constraints:
            constraint.each_event(event)
    feasible = True
    for constraint in constraints:
        fitness += constraint.get_final_fitness()
        if constraint.is_hard_constraint:
            feasible = False if not constraint.indiv_is_feasible else feasible
    indiv.is_feasible = feasible
    return fitness

def get_constraints(state: State) -> List[Constraint]:
    return [CrewDay(state), NoEventOverlap(state), FairWorkHours(state), UndesirableShifts(state),
            LastODO(state)]

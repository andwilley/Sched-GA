"""
Functions relating to fitness calculation.
"""

from typing import List
from app.models.individual import Individual
from app.models.state import State
from app.models.constraints.constraint import Constraint
from app.models.constraints.crew_day import CrewDay
from app.models.constraints.no_event_overlap import NoEventOverlap
from app.models.constraints.fair_work_hours import FairWorkHours
from app.models.constraints.undesirable_shifts import UndesirableShifts
from app.models.constraints.last_odo import LastODO

def calc_fitness(indiv: Individual, *constraints: Constraint) -> float:
    """
    Calculates an individual's fitness based on the passed constraints.
    Mutates indiv (is_feasible field)

    Args:
        indiv: the Individual to calculate fitness for.
        constraints: an array of Constraint sub-class instances.

    Returns:
        The fitness of the individual.
    """

    fitness = 0.0

    # run each event for each constraint on every event in the individual
    for event in indiv.schedule:
        for constraint in constraints:
            constraint.each_event(event)
    feasible = True

    # sum the fitness for each constraint
    for constraint in constraints:
        fitness += constraint.get_final_fitness()
        if constraint.is_hard_constraint:
            feasible = False if not constraint.indiv_is_feasible else feasible
    indiv.is_feasible = feasible
    return fitness

def get_constraints(state: State) -> List[Constraint]:
    """
    Builds the constraint array.

    Args:
        state: the application state object.

    Returns:
        A list of constraints.
    """

    return [CrewDay(state), NoEventOverlap(state), FairWorkHours(state), UndesirableShifts(state),
            LastODO(state)]

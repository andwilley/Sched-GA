import unittest
from typing import Tuple
import numpy as np
from app.state.events_big import events
from app.state.pilots_big import pilots
from app.models.state import State
from app.models.population import Population
from app.models.constraints.no_event_overlap import NoEventOverlap
from app.models.constraints.crew_day import CrewDay
from app.models.constraints.fair_work_hours import FairWorkHours
from app.models.constraints.undesirable_shifts import UndesirableShifts
from app.models.constraints.constraint import Constraint
from app.ga.fitness import calc_fitness

class FindWeightsCase(unittest.TestCase):

    @staticmethod
    def get_avg_constraint_fitness(pop: Population, constraint: Constraint) -> Tuple[float, float]:
        max_penalty = 0.0
        fits = np.array([])
        for indiv in pop.population:
            fit = calc_fitness(indiv, constraint)
            fits = np.append(fits, fit)
            if fit > max_penalty:
                max_penalty = fit
        return max_penalty, np.average(fits)

    def test_find_weights(self):
        state = State(pilots, events)
        pop = Population(1000, .1, True, 1, .01, state)
        crew_day = self.get_avg_constraint_fitness(pop, CrewDay(state))
        overlap = self.get_avg_constraint_fitness(pop, NoEventOverlap(state))
        fair_hours = self.get_avg_constraint_fitness(pop, FairWorkHours(state))
        undesirable = self.get_avg_constraint_fitness(pop, UndesirableShifts(state))

        print("crewday: ", crew_day)
        print("overlap: ", overlap)
        print("fair_hours: ", fair_hours)
        print("undesirable: ", undesirable)

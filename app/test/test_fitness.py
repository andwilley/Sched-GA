import unittest
from app.ga.parameters import OVERLAP_WEIGHT
from app.ga.fitness import calc_fitness, get_constraints
from app.models.state import State
from app.models.individual import Individual
from app.models.constraints.no_event_overlap import NoEventOverlap
from app.test.test_state import spec_events, spec_pilots, spec_indiv

class FitnessCase(unittest.TestCase):
    def test_specific_individual_fitness(self):
        state = State(spec_pilots, spec_events)
        no_overlap_constraint = NoEventOverlap(state)
        indiv = Individual(state).spawn(spec_indiv)

        fitness = calc_fitness(indiv, no_overlap_constraint)

        self.assertEqual(fitness, 180 * OVERLAP_WEIGHT, "Fitness should be 180.")

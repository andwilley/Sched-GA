import unittest
import uuid
from app.models.individual import Individual
from app.models.state import State
from app.test.test_state import schedule, sched_alleles, op_events, op_pilots

class IndividualCase(unittest.TestCase):

    def test_init_and_setters(self):
        state = State(op_pilots, op_events)
        indiv1 = Individual(state)
        indiv2 = Individual(state)
        indiv3 = Individual(state)
        self.assertIsNotNone(indiv1.schedule[0].event_id, "Schedule should be set.")
        self.assertTrue(isinstance(indiv1.schedule[0].pilot_id, uuid.UUID), "Pilot should be set")

        indiv1.fitness = 1
        self.assertEqual(indiv1.fitness, 1, "Fitness should be set.")
        indiv2.fitness = 3
        indiv3.fitness = 3

        self.assertTrue(indiv1 < indiv2, "first should be less than second")
        self.assertTrue(indiv2 == indiv3, "second should be equal to third")

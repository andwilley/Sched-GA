import unittest
import uuid
from app.models.individual import Individual
from app.test.test_state import schedule, uuid1

class IndividualCase(unittest.TestCase):

    def test_init_and_setters(self):
        indiv1 = Individual(schedule)
        indiv2 = Individual(schedule)
        indiv3 = Individual(schedule)
        self.assertEqual(indiv1.schedule[0].event_id, uuid1, "Schedule should be set.")
        self.assertTrue(isinstance(indiv1.schedule[0].pilot_id, uuid.UUID), "Pilot should be set")

        indiv1.fitness = 1
        self.assertEqual(indiv1.fitness, 1, "Fitness should be set.")
        indiv2.fitness = 3
        indiv3.fitness = 3

        self.assertTrue(indiv1 < indiv2, "first should be less than second")
        self.assertTrue(indiv2 == indiv3, "second should be equal to third")

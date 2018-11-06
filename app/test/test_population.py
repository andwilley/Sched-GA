import unittest
from app.models.population import Population
from app.test.test_state import pop_sched as schedule

class PopulationCase(unittest.TestCase):

    def test_initialize(self):
        pop = Population(10, .1, schedule)
        self.assertEqual(pop.max_fitness, 0, "Max fitness should init to 0")
        self.assertEqual(pop.elite_size, 1, "Elite size should be 1")

        pop.size = 20
        self.assertEqual(pop.size, 10, "Size should not change")

    def test_set_fitness(self):
        pop = Population(10, .1, schedule)

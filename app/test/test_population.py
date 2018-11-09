import unittest
from app.models.population import Population
from app.models.state import State
from app.test.test_state import pop_sched, pop_pilots, pop_events, pop_sched_alleles

class PopulationCase(unittest.TestCase):
    POP_SIZE = 10
    ELITE_RATIO = .1

    def test_initialize(self):
        state = State(pop_pilots, pop_events, pop_sched, pop_sched_alleles)
        pop = Population(self.POP_SIZE, self.ELITE_RATIO, state=state)
        self.assertEqual(pop.max_fitness, 0, "Max fitness should init to 0")
        self.assertEqual(pop.elite_size, 1, "Elite size should be 1")

        pop.size = 20
        self.assertEqual(pop.size, self.POP_SIZE, "Size should not change")

    def test_set_fitness(self):
        state = State(pop_pilots, pop_events, pop_sched, pop_sched_alleles)
        pop = Population(self.POP_SIZE, self.ELITE_RATIO, state=state)
        pop.set_fitness()
        print("\n\nTest fitness")
        for indiv in pop.population:
            print(indiv)
        print(pop.elites)

    def test_make_next_gen(self):
        state = State(pop_pilots, pop_events, pop_sched, pop_sched_alleles)
        pop = Population(self.POP_SIZE, self.ELITE_RATIO, state=state)
        pop.set_fitness()
        elite = pop.elites[0]
        print("\n\nFirst pop")
        for indiv in pop.population:
            print(indiv)
        pop.make_next_generation()
        pop.set_fitness()
        self.assertTrue(elite in pop.population, "The elite should be carried forward")
        self.assertEqual(len(pop.population), self.POP_SIZE, "Should not change size")
        print("\n\nNew pop")
        for indiv in pop.population:
            print(indiv)
        print(pop.elites)

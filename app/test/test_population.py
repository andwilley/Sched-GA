import unittest
from typing import Any
from app.models.population import Population
from app.models.state import State
from app.test.state.population_test import pop_pilots, pop_events

class PopulationCase(unittest.TestCase):
    POP_SIZE = 10
    ELITE_RATIO = .3
    X_OVER_PNTS = 1
    MUT_PROB = 0.1
    snivs: Any = {}

    def test_initialize(self):
        state = State(pop_pilots, pop_events, self.snivs)
        pop = Population(self.POP_SIZE, self.ELITE_RATIO, True, self.X_OVER_PNTS, self.MUT_PROB,
                         state=state)
        self.assertEqual(pop.max_fitness, 0, "Max fitness should init to 0")
        self.assertEqual(pop.elite_size, 3, "Elite size should be 1")
        pop.size = 20
        self.assertEqual(pop.size, self.POP_SIZE, "Size should not change")

    def test_set_fitness(self):
        state = State(pop_pilots, pop_events, self.snivs)
        pop = Population(self.POP_SIZE, self.ELITE_RATIO, True, self.X_OVER_PNTS, self.MUT_PROB,
                         state=state)
        pop.set_fitness()
        self.assertEqual(len(pop.elites), pop.elite_size, "Elites should be correct size")
        print("\n\nTest fitness")
        at_least_one_is_not_zero = False
        for indiv in pop.population:
            at_least_one_is_not_zero = True if indiv.fitness > 0 else at_least_one_is_not_zero
            print(indiv)
        self.assertTrue(at_least_one_is_not_zero, "fitness should be set for the population")
        sorted_pop = sorted(pop.population)
        self.assertEqual(pop.elites, sorted_pop[:pop.elite_size], "elites should be the best")


    def test_make_next_gen(self):
        state = State(pop_pilots, pop_events, self.snivs)
        pop = Population(self.POP_SIZE, self.ELITE_RATIO, True, self.X_OVER_PNTS, self.MUT_PROB,
                         state=state)
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

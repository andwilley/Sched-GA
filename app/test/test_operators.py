import unittest
import random as rnd
from app.ga.operators import roulette_selection, create_and_mutate_offspring, crossover, mutate
from app.models.individual import Individual
from app.test.test_state import schedule

class OperatorsCase(unittest.TestCase):

    def test_mutate(self):
        """
        Test the mutation operator.
        Test is the console output. This is lazy.
        """
        indiv1 = Individual(schedule)
        print(indiv1)
        mut1 = mutate(indiv1, 1.0)
        print(mut1)

    def test_crossover(self):
        """
        Test the crossover operator.
        """
        parent1 = Individual(schedule)
        parent2 = Individual(schedule)
        xovers = 2

        child1, child2 = crossover(parent1, parent2, xovers)

        for i, gene in enumerate(child1.schedule):
            self.assertTrue(gene.pilot_id == parent1.schedule[i].pilot_id or
                            gene.pilot_id == parent2.schedule[i].pilot_id,
                            "should only contain genes from parent")

        for i, gene in enumerate(child2.schedule):
            self.assertTrue(gene.pilot_id == parent1.schedule[i].pilot_id or
                            gene.pilot_id == parent2.schedule[i].pilot_id,
                            "should only contain genes from parent")

        # print("parent 1: " + str(parent1))
        # print("parent 2: " + str(parent2))
        # print(" child 1: " + str(child1))
        # print(" child 2: " + str(child2))

    def test_offspring(self):
        """
        Test the create offspring operator for odd and even num parents
        """
        num_parents = 5

        parents = []
        for _ in range(num_parents):
            parents.append(Individual(schedule))

        children = create_and_mutate_offspring(parents, 1, 0.5)
        self.assertEqual(len(children), num_parents, "children should be the same size as parents")

        parents.append(Individual(schedule))
        children = create_and_mutate_offspring(parents, 1, 0.5)
        self.assertEqual(len(children), num_parents + 1, "children should be the same size as\
            parents")

    def test_roulette(self):
        """
        Test roulette selection. This should test for proportional probability.
        """
        num_indivs = 10
        num_parents = 9

        population = []
        for _ in range(num_indivs):
            new_indiv = Individual(schedule)
            new_indiv.fitness = rnd.uniform(0, num_parents)
            population.append(new_indiv)

        selection = roulette_selection(population, num_parents)
        self.assertEqual(len(selection), num_parents, "should corrent number of parents")

        pop_avg_fit = sum([indiv.fitness for indiv in population])
        sel_avg_fit = sum([indiv.fitness for indiv in selection])
        self.assertGreater(sel_avg_fit, pop_avg_fit, "new selection fitness should be higher")

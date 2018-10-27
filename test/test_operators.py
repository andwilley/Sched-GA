import unittest
from ga.operators import roulette_selection, create_and_mutate_offspring, crossover, mutate
from models.individual import Individual
from app.state.sched import schedule

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

        print("parent 1: " + str(parent1))
        print("parent 2: " + str(parent2))
        print(" child 1: " + str(child1))
        print(" child 2: " + str(child2))

    def test_offspring(self):
        """
        Test the create offspring operator.
        """
        parent1 = Individual(schedule)
        parent2 = Individual(schedule)

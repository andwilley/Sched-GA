import unittest
from ga.operators import roulette_selection, create_and_mutate_offspring, crossover, mutate
from models.individual import Individual
from app.state.sched import schedule
class OperatorsCase(unittest.TestCase):

    def test_mutate(self):
        indiv1: Individual = Individual(schedule)
        indiv2: Individual = Individual(schedule)

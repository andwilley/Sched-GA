import random as rnd
from typing import List, Tuple
from bisect import insort
from models.population import Population
from models.individual import Individual

# operates on population as a list of individuals



def roulette_selection(population: Population) -> Individual:
    """
    Select a parent by roulette (proportional) selection
    """
    max_fitness = population.max_fitness
    pick = rnd.uniform(0, max_fitness)
    current = 0
    for individual in population.population:
        current += individual.fitness
        if current > pick:
            return individual
    # if we don't get a value, return the last item
    return population.population[len(population.population) - 1]

def create_and_mutate_offspring(parents: List[Individual], points: int,
                                mutate_prob: float) -> List[Individual]:
    children: List[Individual] = []
    for i in range(0, len(parents), 2):
        j = i + 1 if i + 1 < len(parents) else 0
        child1, child2 = crossover(parents[i], parents[j], points)
        children.append(child1)
        children.append(child2)
        # TODO mutate
    return children

def crossover(parent1: Individual, parent2: Individual, pnts: int) -> Tuple[Individual, Individual]:
    """
    Peform crossover on parent1 and parent2 to create 2 children.
    Params:
        parent1: first parent
        parent2: second parent
        pnts: number of pnts to cross over at. set to length of parent for uniform.
    Return: 2 children
    """
    xovers: List[int] = []
    for _ in range(pnts):
        insort(xovers, rnd.uniform(0, len(parent1) - 1))
    child1, child2 = parent1.schedule, parent2.schedule
    for xover, i in enumerate(xovers):
        assign_to_child1 = parent1.schedule if i % 2 else parent2.schedule
        assign_to_child2 = parent2.schedule if i % 2 else parent1.schedule
        child1 = child1[0:xover] + assign_to_child1[xover:]
        child2 = child2[0:xover] + assign_to_child2[xover:]
    return Individual(child1), Individual(child2)

def mutate():
    pass

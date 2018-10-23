import random as rnd
from typing import List, Tuple
from bisect import insort
from models.individual import Individual
from models.eventGene import EventGene

# operates on population as a list of individuals

def roulette_selection(population: List[Individual]) -> Individual:
    """
    Select a parent by roulette (proportional) selection
    """
    sum_fit = sum([indiv.fitness for indiv in population])
    pick = rnd.uniform(0, sum_fit)
    current = 0
    for individual in population:
        current += individual.fitness
        if current > pick:
            return individual
    # if we don't get a value, return the last item. this should be exceedingly rare.
    return population[len(population) - 1]

def create_and_mutate_offspring(parents: List[Individual], points: int,
                                mutate_prob: float) -> List[Individual]:
    children: List[Individual] = []
    for i in range(0, len(parents), 2):
        # if theres an odd number, use the first parent again
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
    child1: List[EventGene] = parent1.schedule
    child2: List[EventGene] = parent2.schedule
    for xover, i in enumerate(xovers):
        assign_to_child1 = parent1.schedule if i % 2 else parent2.schedule
        assign_to_child2 = parent2.schedule if i % 2 else parent1.schedule
        child1 = child1[:xover] + assign_to_child1[xover:]
        child2 = child2[:xover] + assign_to_child2[xover:]
    return Individual(child1), Individual(child2)

def mutate(indiv: Individual, prob: float) -> Individual:
    if not 0 <= prob <= 1:
        raise ValueError("mutate prob must be a value between 0 and 1.")
    for gene in indiv.schedule:
        pick = rnd.uniform(0, 1)
        if prob > pick:
            alele_last_index = len(sched_aleles[gene.eventId] - 1)
            gene.pilotId = sched_aleles[gene.eventId][rnd.randint(0, alele_last_index)]
    return indiv

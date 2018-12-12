"""
Functions defining or relating to genetic operators.
"""

import random as rnd
from typing import List, Tuple
from bisect import insort
from app.models.individual import Individual
from app.models.event_gene import EventGene

# operates on population as a list of individuals

def roulette_selection(population: List[Individual], num_parents: int) -> List[Individual]:
    """
    Select specified num parents by roulette (proportional) selection

    Args:
        population: list of individuals to select from.
        num_parents: number of parents to select.

    Returns:
        A new list of individuals, the parents.
    """

    sum_fit = sum([indiv.inverse_fitness for indiv in population])

    parents = []
    for _ in range(num_parents):
        parents.append(roulette_select_one(population, sum_fit))
    return parents

def roulette_select_one(population: List[Individual], sum_fit: float) -> Individual:
    """
    Select one parent via roulette.

    Args:
        population: the list of individuals to select from
        sum_fit: the sum of the fitness values for calculation of proportional probability

    Returns:
        The selected Individual.
    """

    pick = rnd.uniform(0, sum_fit)
    current = 0.0
    for individual in population:
        current += individual.inverse_fitness
        if current > pick:
            return individual
    # if we don't get a value, return the first item. this should be exceedingly rare.
    return population[0]

def create_and_mutate_offspring(parents: List[Individual],
                                points: int,
                                mutate_prob: float) -> List[Individual]:
    """
    Create offspring from a list of parents and mutatate those offspring with a certain
    probability. Loops through parents in order, mating each adjacent parent and creating
    two offspring. If there are an odd number of parents, pair the last with the first.

    Args:
        parents: a list of Individuals, the parents.
        points: number of crossover points.
        mutate_prob: the probability of mutation for each gene.

    Returns:
        The list of offspring of the same length as the parents, the new population.
    """

    children: List[Individual] = []
    for i in range(0, len(parents), 2):
        # if theres an odd number, use the first parent again
        j = i + 1 if i + 1 < len(parents) else 0
        child1, child2 = crossover(parents[i], parents[j], points)
        children.append(mutate(child1, mutate_prob))
        if i + 1 < len(parents):
            children.append(mutate(child2, mutate_prob))
    return children

def crossover(parent1: Individual, parent2: Individual, pnts: int) -> Tuple[Individual, Individual]:
    """
    Peform crossover on parent1 and parent2 to create 2 children.

    Args:
        parent1: first parent to crossover.
        parent2: second parent to crossover.
        pnts: number of pnts to cross over at. set to length of parent for uniform.

    Returns:
        2 child Individuals as a tuple
    """

    if pnts >= len(parent1):
        raise ValueError("cross over points must be smaller than the size of the array")
    xovers: List[int] = []
    for _ in range(pnts):
        insort(xovers, rnd.randint(0, len(parent1) - 1))

    child1: List[EventGene] = []
    child2: List[EventGene] = []
    use_prnt1 = True
    for i, _ in enumerate(parent1.schedule):
        if xovers and i == xovers[0]:
            use_prnt1 = not use_prnt1
            del xovers[0]
        child1.append(parent1.schedule[i].copy() if use_prnt1 else parent2.schedule[i].copy())
        child2.append(parent1.schedule[i].copy() if not use_prnt1 else parent2.schedule[i].copy())
    return parent1.spawn(child1), parent2.spawn(child2)

def mutate(indiv: Individual, prob: float) -> Individual:
    """
    Mutates each event in the gene with a probability of prob.
    Actually mutates the passed Individual object.

    Args:
        indiv: the individual to mutate.
        prob: the probability as a decimal with which to mutate.

    Returns:
        The same individual with updated genes after mutation
    """

    if not 0 <= prob <= 1:
        raise ValueError("mutate prob must be a value between 0 and 1.")
    for gene in indiv.schedule:
        pick = rnd.uniform(0, 1)
        if prob >= pick:
            indiv.assign_rand_pilot(gene)
    return indiv

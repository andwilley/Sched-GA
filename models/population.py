from typing import List
from bisect import insort
from models.individual import Individual
from ga.fitness import calc_fitness
from ga.operators import roulette_selection, create_and_mutate_offspring

class Population():

    def __init__(self, size: int, elite_percent: int):
        """
        Creates a list of random individuals as the population
        """
        if not 0 <= elite_percent <= 100:
            raise ValueError("elite_percent must be between 0 and 100")

        self.size = size
        self.population = [Individual() for i in range(self.size)] # list of random individuals
        self.elite_size = int(elite_percent * self.size)
        self.elites: List[Individual] = []
        self.max_fitness = 0

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if self.size:
            return
        self._size = size

    @property
    def population(self) -> List[Individual]:
        return self._population

    @population.setter
    def population(self, population: List[Individual]):
        if len(population) != self.size:
            raise ValueError("Invalid population size.")
        self._population: List[Individual] = population

    @property
    def elites(self) -> List[Individual]:
        return self._elites

    @elites.setter
    def elites(self, elites: List[Individual]):
        self._elites = elites

    @property
    def elite_size(self) -> int:
        return self._elite_size

    @elite_size.setter
    def elite_size(self, elite_size):
        self._elite_size = elite_size

    def merge_and_set_populations(self, pop1: List[Individual], pop2: List[Individual]):
        if len(pop1) + len(pop2) != self.size:
            raise ValueError("Invalid population size.")
        self.population = pop1 + pop2

    def set_fitness(self):
        """
        Calculates and sets the fitness of each individual in the population
        """
        self.elites = []
        for indiv in self.population:
            indiv.fitness = calc_fitness(indiv)
            # fill up elites
            if len(self.elites) < self.elite_size:
                insort(self.elites, indiv)
            # if elites is full, push one out if this one is better
            elif indiv.fitness < self.elites[self.elite_size - 1].fitness:
                insort(self.elites, indiv)
                del self.elites[self.elite_size]
            # save the max to invert the fitness and for proportional selection
            if indiv.fitness > self.max_fitness:
                self.max_fitness = indiv.fitness

        # run through one more time to invert the fitness
        self._invert_fitness()

    def _invert_fitness(self):
        for indiv in self.population:
            indiv.fitness = self.max_fitness - indiv.fitness

    def make_next_generation(self):
        """
        Replaces the population with the next generation using GA operators
        """
        next_pop: List[Individual] = []
        parents: List[Individual] = []
        children: List[Individual] = []

        # push the elites forward
        for elite in self.elites:
            next_pop.append(elite)

        # select parents
        for _ in range(len(next_pop), self.size):
            parents.append(roulette_selection(self.population))

        children = create_and_mutate_offspring(parents, points=2, mutate_prob=0.1)
        # calc offspring fitness
        # merge elites and offspring into new population
        pass

from typing import List
from bisect import insort
from app.models.individual import Individual
from app.ga.fitness import calc_fitness, get_constraints
from app.ga.operators import roulette_selection, create_and_mutate_offspring
from app.models.state import State
from app.ga.parameters import X_OVER_PTS, MUT_PROB

class Population():

    def __init__(self, size: int, elite_ratio: float, state: State):
        """
        Creates a list of random individuals as the population
        """
        if not 0 <= elite_ratio <= 1:
            raise ValueError("elite_ratio must be between 0 and 100")

        self.size = size
        self.population = [Individual(state=state) for i in range(self.size)]
        self.elite_size = int(elite_ratio * self.size)
        self.elites: List[Individual] = []
        self.max_fitness = 0
        self._state = state

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, size: int) -> None:
        if hasattr(self, '_size'):
            return
        self._size = size

    @property
    def population(self) -> List[Individual]:
        return self._population

    @population.setter
    def population(self, population: List[Individual]) -> None:
        if len(population) != self.size:
            raise ValueError("Invalid population size.")
        self._population: List[Individual] = population

    @property
    def elites(self) -> List[Individual]:
        return self._elites

    @elites.setter
    def elites(self, elites: List[Individual]) -> None:
        self._elites = elites

    @property
    def elite_size(self) -> int:
        return self._elite_size

    @elite_size.setter
    def elite_size(self, elite_size: int) -> None:
        self._elite_size = elite_size

    def merge_and_set_populations(self, pop1: List[Individual], pop2: List[Individual]):
        if len(pop1) + len(pop2) != self.size:
            raise ValueError("Invalid population size.")
        self.population = pop1 + pop2

    def set_fitness(self) -> None:
        """
        Calculates and sets the fitness of each individual in the population
        """
        self.elites = []
        self.max_fitness = 0
        for indiv in self.population:
            indiv.fitness = calc_fitness(indiv, *get_constraints(self._state))
            # fill up elites
            if len(self.elites) < self.elite_size:
                insort(self.elites, indiv)
            # if elites is full, push one out if this one is better
            elif self.elite_size > 0 and indiv.fitness < self.elites[self.elite_size - 1].fitness:
                insort(self.elites, indiv)
                del self.elites[self.elite_size]
            # save the max to invert the fitness and for proportional selection
            if indiv.fitness > self.max_fitness:
                self.max_fitness = indiv.fitness

        # run through one more time to invert the fitness
        self._invert_fitness()

    def _invert_fitness(self) -> None:
        for indiv in self.population:
            indiv.fitness = self.max_fitness - indiv.fitness

    def make_next_generation(self) -> None:
        """
        Replaces the population with the next generation using GA operators
        """
        # select parents
        parents = roulette_selection(self.population, self.size - self.elite_size)

        # make children
        children = create_and_mutate_offspring(parents, points=X_OVER_PTS, mutate_prob=MUT_PROB)

        # add elites and set population
        self.population = self.elites + children

    def __repr__(self):
        return "(Population: )"

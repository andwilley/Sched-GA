from bisect import insort
from math import inf
from typing import List, Set
from app.models.state import State
from app.models.individual import Individual
from app.ga.fitness import calc_fitness, get_constraints
from app.ga.operators import roulette_selection, create_and_mutate_offspring

class Population():

    def __init__(self, size: int, elite_ratio: float, diverse_elite: bool, x_ovr_pts: int,
                 mut_prb: float, state: State):
        """
        Creates a list of random individuals as the population
        """
        if not 0 <= elite_ratio <= 1 or not 0 <= mut_prb <= 1 or x_ovr_pts < 0 or size < 1:
            raise ValueError("One or more arguments for Population is outside the allowed range.")

        self.size = size
        self.population = [Individual(state=state) for i in range(self.size)]
        self.elite_size = int(elite_ratio * self.size)
        self.elites: List[Individual] = []
        self.max_fitness = 0.0
        self.min_fitness = inf
        self._state = state
        self._x_ovr_pts = x_ovr_pts
        self._mut_prb = mut_prb
        self._elite_set: Set[str] = set()
        self._diverse_elite = diverse_elite

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

    @property
    def max_fitness(self) -> float:
        return self._max_fitness

    @max_fitness.setter
    def max_fitness(self, fitness: float) -> None:
        self._max_fitness = fitness

    def merge_and_set_populations(self, pop1: List[Individual], pop2: List[Individual]):
        if len(pop1) + len(pop2) != self.size:
            raise ValueError("Invalid population size.")
        self.population = pop1 + pop2

    @property
    def min_fitness(self) -> float:
        return self._min_fitness

    @min_fitness.setter
    def min_fitness(self, fitness: float) -> None:
        self._min_fitness = fitness

    def set_fitness(self) -> None:
        """
        Calculates and sets the fitness of each individual in the population.
        Maintains the elites array with the best solutions found.
        If diverse elites is true, enforces uniqueness in elites.
        """
        self.max_fitness = 0.0
        for indiv in self.population:
            indiv.inverse_fitness = 0
            indiv.fitness = calc_fitness(indiv, *get_constraints(self._state))
            # fill up elites
            if ((len(self.elites) < self.elite_size)
                    and ((self._diverse_elite and indiv.crew_string() not in self._elite_set)
                         or not self._diverse_elite)):
                insort(self.elites, indiv)
                if self._diverse_elite:
                    self._elite_set.add(indiv.crew_string())
            # if elites is full, push one out if this one is better
            elif ((self.elite_size > 0 and indiv.fitness < self.elites[self.elite_size - 1].fitness)
                  and ((self._diverse_elite and indiv.crew_string() not in self._elite_set)
                       or not self._diverse_elite)):
                insort(self.elites, indiv)
                if self._diverse_elite:
                    self._elite_set.add(indiv.crew_string())
                    self._elite_set.remove(self.elites[self.elite_size].crew_string())
                del self.elites[self.elite_size]
            # save the max to invert the fitness, for proportional selection
            if indiv.fitness > self.max_fitness:
                self.max_fitness = indiv.fitness
            # save the min for analysis
            if indiv.fitness < self.min_fitness:
                self.min_fitness = indiv.fitness

        # run through one more time to invert the fitness
        self._invert_fitness()

    def _invert_fitness(self) -> None:
        for indiv in self.population:
            indiv.inverse_fitness = self.max_fitness - indiv.fitness

    def make_next_generation(self) -> None:
        """
        Replaces the population with the next generation using GA operators
        """
        # select parents
        parents = roulette_selection(self.population, self.size - self.elite_size)

        # make children
        children = create_and_mutate_offspring(parents, points=self._x_ovr_pts,
                                               mutate_prob=self._mut_prb)

        # add elites and set population
        self.population = self.elites + children

    def get_feasible_count(self) -> int:
        feasible_count = 0
        for indiv in self.population:
            if indiv.is_feasible:
                feasible_count += 1
        return feasible_count

    def __repr__(self) -> str:
        return "(Population: {})".format(self.population)

"""
The Individual Model.
"""

from typing import List
from copy import deepcopy
import random as rnd
from app.models.event_gene import EventGene
from app.models.state import State

class Individual():
    """
    Individual represents a single chromosome
    """

    def __init__(self, state: State, fill: bool = True) -> None:
        """
        Creates the individual

        Args:
            state: application state object
            fill: True will pick pilots at random for each event. False leaves that field set,
                intended to for use when creating a crossedover child.

        Returns:
            None
        """

        self.schedule = deepcopy(state.schedule)
        self.fitness = 0.0
        self.inverse_fitness = 0.0
        self.is_feasible = True
        self._state = state
        if fill:
            for gene in self.schedule:
                self.assign_rand_pilot(gene)

    @property
    def schedule(self) -> List[EventGene]:
        return self._schedule

    @schedule.setter
    def schedule(self, schedule: List[EventGene]):
        self._schedule = schedule

    @property
    def fitness(self) -> float:
        return self._fitness

    @fitness.setter
    def fitness(self, fitness: float):
        if fitness < 0:
            fitness = 0
        self._fitness = fitness

    @property
    def inverse_fitness(self) -> float:
        return self._inverse_fitness

    @inverse_fitness.setter
    def inverse_fitness(self, fitness: float) -> None:
        if fitness < 0:
            fitness = 0
        self._inverse_fitness = fitness

    @property
    def is_feasible(self) -> bool:
        return self._is_feasible

    @is_feasible.setter
    def is_feasible(self, feasible: bool) -> None:
        self._is_feasible = feasible

    def assign_rand_pilot(self, gene: EventGene) -> None:
        """
        Assign random pilot to the passed gene from the event allele.

        Args:
            gene: the event gene to assign a random pilot to

        Returns:
            None (mutates the gene instance)
        """

        allele_last_index = len(self._state.alleles[gene.event_id]) - 1
        gene.pilot_id = self._state.alleles[gene.event_id][rnd.randint(0, allele_last_index)]

    def spawn(self, new_sched: List[EventGene]) -> 'Individual':
        """
        Create a new individual from a modified schedule (xover or mutation done externally)

        Args:
            new_sched: the new event list to assign to this Individual, should come from a
                crossover or mutation. Must match the event order of the schedule in State.

        Returns:
            A new Individual.
        """
        indiv = Individual(self._state, fill=False)
        indiv.schedule = new_sched
        return indiv

    def crew_string(self) -> str:
        """
        Creates a string to represent each pilot in order of events in this schedule.

        Returns:
            a string of 32 char hex IDs for each pilot in every event.
        """

        cstr = ''
        for gene in self.schedule:
            cstr += gene.pilot_id.hex
        return cstr

    def __lt__(self, other):
        return self.fitness < other.fitness

    def __le__(self, other):
        return self.fitness <= other.fitness

    def __eq__(self, other):
        return self.fitness == other.fitness

    def __ge__(self, other):
        return self.fitness >= other.fitness

    def __gt__(self, other):
        return self.fitness > other.fitness

    def __ne__(self, other):
        return self.fitness != other.fitness

    def __len__(self):
        return len(self.schedule)

    def __repr__(self):
        schedule = []
        for gene in self.schedule:
            schedule.append("event start {}, end {}, desc {},\tpilot {},\tqual_req {}".
                            format(self._state.events[gene.event_id].start,
                                   self._state.events[gene.event_id].end,
                                   self._state.events[gene.event_id].desc,
                                   self._state.pilots[gene.pilot_id].callsign,
                                   self._state.events[gene.event_id].qual_req))
        schedule = "\n".join(schedule)
        return "(Individual: schedule \n{}, fitness {}, {})".format(schedule, self.fitness,\
            "feasible" if self.is_feasible else "INFEASIBLE")

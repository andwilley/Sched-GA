from typing import List
from copy import deepcopy
import random as rnd
from app.models.event_gene import EventGene
# from app.state.sched import sched_alleles
from app.test.test_state import pop_sched_alleles as sched_alleles

class Individual():
    """
    Individual represents a single chromosome

    Attributes:
        schedule: an array of event and pilot ids
        fitness: the penalty score of this individual
    """
    def __init__(self, schedule: List[EventGene], fill: bool = True) -> None:
        self.schedule = deepcopy(schedule)
        self.fitness = 0
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
    def fitness(self) -> int:
        return self._fitness

    @fitness.setter
    def fitness(self, fitness: int):
        if fitness < 0:
            fitness = 0
        self._fitness = fitness

    def assign_rand_pilot(self, gene: EventGene) -> None:
        """
        Assign random pilot to the passed gene from the event allele.
        """
        allele_last_index = len(sched_alleles[gene.event_id]) - 1
        gene.pilot_id = sched_alleles[gene.event_id][rnd.randint(0, allele_last_index)]

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
        return "schedule {}, fitness {}".format(self.schedule, self.fitness)

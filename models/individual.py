from typing import List, Dict
import random as rnd
from models.event_gene import EventGene
from models.pilot import Pilot

class Individual():
    """
    Individual represents a single chromosome

    Attributes:
        schedule - an array of events and pilots
        fitness - the penalty score of this individual
    """
    def __init__(self, schedule: List[EventGene],
                 sched_alleles: Dict[str, List[Pilot]] = None) -> None:
        if sched_alleles:
            for gene in schedule:
                self.assign_rand_pilot(gene)
        else:
            self.schedule = schedule
        self.sched_alleles = sched_alleles
        self.fitness = 0

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

    @property
    def sched_alleles(self):
        return self._sched_alleles

    @sched_alleles.setter
    def sched_alleles(self, sched_alleles: Dict[str, List[Pilot]]):
        self._sched_alleles = sched_alleles

    def assign_rand_pilot(self, gene: EventGene):
        """
        Assign random pilot to the passed gene from the event allele.
        """
        allele_last_index = len(self.sched_alleles[gene.event_id]) - 1
        gene.pilot_id = self.sched_alleles[gene.event_id][rnd.randint(0, allele_last_index)].id

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
        return "value {}, fitness {}".format(self.schedule, self.fitness)

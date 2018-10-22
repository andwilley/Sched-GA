from typing import List
from models.eventGene import EventGene

class Individual():
    """
    Individual represents a single chromosome

    Attributes:
        schedule - an array of events and pilots
        fitness - the penalty score of this individual
    """
    def __init__(self, schedule: List[EventGene] = None):
        if schedule:
            self.schedule = schedule
        else:
            # randomly gen schedule
            pass
        self.fitness = 0

    @property
    def fitness(self):
        return self._fitness

    @fitness.setter
    def fitness(self, fitness: int):
        self._fitness = fitness

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

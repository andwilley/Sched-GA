import abc
from models.event_gene import EventGene

class Constraint(abc.ABC):
    """
    ABC for constraints. Inhereting classes must implement the below methods

    An instance of the inhereting class is passed to the fitness function each
    time an individual is evaluated.

    For each event, the "each_event" method of the inhereting class is called.

    Once each event is passed to the class, the "get_fitness" method is called
    to record each constraint's addition to the individual's fitness.

    Try to avoid saving the individual and looping over it again to calculate
    the fitness. If every constraint does this, it creates a performance hit.

    Attributes:
    """

    @abc.abstractmethod
    def each_event(self, gene: EventGene) -> None:
        pass

    @abc.abstractmethod
    def get_final_fitness(self) -> int:
        pass

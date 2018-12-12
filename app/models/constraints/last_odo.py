"""
Last ODO fairness Constraint
"""

from app.models.constraints.constraint import Constraint
from app.models.event_gene import EventGene
from app.models.state import State
from app.constants.event_types import ODO
# this should be passed as a parameter:
from app.ga.parameters import LAST_ODO_WEIGHT

class LastODO(Constraint):
    """
    Last ODO constraint. Penalizes pilots scheduled for ODO based on their days since last ODO.
    The higher the days since last ODO, the smaller the penalty.
    """

    def __init__(self, state: State):
        """
        Create the constraint.

        Args:
            state: the application state

        Returns:
            None
        """

        self._fitness = 0.0
        self._state = state

    def each_event(self, gene: EventGene) -> None:
        """
        Called for each event in the individual.

        Args:
            gene: the EventGene to evaluate

        Returns:
            None
        """

        if self._state.events[gene.event_id].desc == ODO:
            self._fitness += 1 - self._state.pilots[gene.pilot_id].last_odo_norm
        # this ended up clutting the fitness a lot. may be useful for recent flight hour constraint.
        # else:
        #     self._fitness += self._state.pilots[gene.pilot_id].last_odo_norm

    def get_final_fitness(self) -> float:
        """
        Returns:
            The fitness calculated with all each_event() calls.
        """
        return self._fitness * LAST_ODO_WEIGHT

    def indiv_is_feasible(self) -> bool:
        return True

    def is_hard_constraint(self) -> bool:
        return False

"""
No event overlap Constraint
"""

from typing import Dict, List
import uuid
from datetime import timedelta
from app.models.constraints.constraint import Constraint
from app.models.event_gene import EventGene
from app.models.state import State
# should be passed as a parameter:
from app.ga.parameters import OVERLAP_WEIGHT

class NoEventOverlap(Constraint):
    """
    No event overlap constraint. Limits pilots to one event at a time.
    Applies penalty (fitness) each time violated. Penalty is minutes of overlap for each event that
    overlaps.
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
        self._pilot_events: Dict[uuid.UUID, List[uuid.UUID]] = {}

    def each_event(self, gene: EventGene) -> None:
        """
        Called for each event in the individual.
        if a pilot has at least 1 event, check to make sure they don't overlap with new event
        need to check each new event against the events already stored (any could overlap)
        it should be linear time through each event for that pilot for each new event
        save each event under a pilot id key

        Fitness is total minutes of overlap.

        This is a performance bottleneck! n^2 ish. each event, each plt (const), each schd event

        Args:
            gene: EventGene to evaluate

        Returns:
            None
        """
        if gene.pilot_id in self._pilot_events:
            for event_id in self._pilot_events[gene.pilot_id]:
                delta: timedelta = min(self._state.events[event_id].end,
                                       self._state.events[gene.event_id].end) - \
                                   max(self._state.events[event_id].start,
                                       self._state.events[gene.event_id].start)
                if delta > timedelta(0):
                    self._fitness += delta.seconds / 60
            self._pilot_events[gene.pilot_id].append(gene.event_id)
        else:
            self._pilot_events[gene.pilot_id] = [gene.event_id]

    def get_final_fitness(self) -> float:
        """
        Returns:
            The fitness calculated with each_event().
        """
        return self._fitness * OVERLAP_WEIGHT

    @property
    def indiv_is_feasible(self) -> bool:
        return True if self._fitness == 0.0 else False

    @property
    def is_hard_constraint(self) -> bool:
        return True

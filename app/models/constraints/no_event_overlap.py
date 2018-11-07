from typing import Dict, List
import uuid
from app.ga.parameters import OVERLAP_WEIGHT
from app.models.constraints.constraint import Constraint
from app.models.event_gene import EventGene
# from app.state.events import events # comment for tests
from app.test.test_state import pop_events as events # use for tests

class NoEventOverlap(Constraint):
    """
    No event overlap constraint. Limits pilots to one event at a time.
    Applies penalty (fitness) each time violated.
    """

    def __init__(self):
        self._fitness = 0
        self._pilot_events: Dict[uuid.UUID, List[uuid.UUID]] = {}

    def each_event(self, gene: EventGene) -> None:
        """
        Called for each event in the individual.
        if a pilot has at least 1 event, check to make sure they don't overlap with new event
        need to check each new event against the events already stored (any could overlap)
        it should be linear through each event for that pilot for each new event
        save each event under a pilot id key
        """
        if gene.pilot_id in self._pilot_events:
            for event_id in self._pilot_events[gene.pilot_id]:
                if max(events[event_id].start, events[gene.event_id].start) < min(
                        events[event_id].end, events[gene.event_id].end):
                    self._fitness += 1
            self._pilot_events[gene.pilot_id].append(gene.event_id)
        else:
            self._pilot_events[gene.pilot_id] = [gene.event_id]

    def get_final_fitness(self) -> int:
        """
        Return the fitness calculated with each_event().
        """
        return self._fitness * OVERLAP_WEIGHT

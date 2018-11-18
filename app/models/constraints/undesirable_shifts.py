from typing import Dict
import uuid
from app.models.state import State
from app.models.constraints.constraint import Constraint
from app.models.event_gene import EventGene
from app.constants.event_types import SIM, ODO, CLS, LSO
from app.constants.opnav import LATE_EVENT
from app.ga.parameters import UNDESIRABLE_SHIFT_WEIGHT as WEIGHT

class UndesirableShifts(Constraint):
    """
    Undesirable shifts constraint. Penalizes scheds with some pilots working much more or less 
    undesirable shifts. Applies a penalty based on difference from the average.
    """

    def __init__(self, state: State):
        self._state = state
        self._crew_tally: Dict[uuid.UUID, int] = {key: 0 for key in self._state.pilots}
        self._total = 0
        self._undesirable_types = [SIM, ODO, CLS, LSO]

    def each_event(self, gene: EventGene) -> None:
        """
        Called for each event in the individual.
        For each event, add the number of undesirable shifts to the pilots tally.
        For now, we use night flights, sims, classes, LSO and ODO.
        """
        if self._state.events[gene.event_id].desc in self._undesirable_types:
            self._crew_tally[gene.pilot_id] += 1
            self._total += 1
        if self._state.events[gene.event_id].end > LATE_EVENT:
            self._crew_tally[gene.pilot_id] += 1
            self._total += 1

    @property
    def indiv_is_feasible(self) -> bool:
        return True

    @property
    def is_hard_constraint(self) -> bool:
        return False

    def get_final_fitness(self) -> float:
        """
        Return the fitness calculated with each_event().
        """
        avg = self._total / len(self._state.pilots)
        return float(WEIGHT) * sum([abs(tally - avg) for _, tally in self._crew_tally.items()])

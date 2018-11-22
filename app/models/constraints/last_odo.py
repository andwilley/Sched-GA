from app.models.constraints.constraint import Constraint
from app.models.event_gene import EventGene
from app.models.state import State
from app.ga.parameters import LAST_ODO_WEIGHT
from app.constants.event_types import ODO

class LastODO(Constraint):
    """
    CrewDay constraint. Limits pilots to DAY_CREW_DAY or NIGHT_CREW_DAY hours per day.
    Applies a penalty if an overage occurs.
    """

    def __init__(self, state: State):
        self._fitness = 0.0
        self._state = state

    def each_event(self, gene: EventGene) -> None:
        """
        Called for each event in the individual.
        """
        if self._state.events[gene.event_id].desc == ODO:
            self._fitness += 1 - self._state.pilots[gene.pilot_id].last_odo_norm
        # else:
        #     self._fitness += self._state.pilots[gene.pilot_id].last_odo_norm

    def get_final_fitness(self) -> float:
        """
        Return the fitness calculated with each_event().
        """
        return self._fitness * LAST_ODO_WEIGHT

    def indiv_is_feasible(self) -> bool:
        return True

    def is_hard_constraint(self) -> bool:
        return False

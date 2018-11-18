from datetime import datetime
from typing import Dict, Tuple
import uuid
from app.models.state import State
from app.models.constraints.constraint import Constraint
from app.models.event_gene import EventGene
from app.ga.parameters import FAIR_HOURS_WEIGHT

class FairWorkHours(Constraint):
    """
    Fair work hours constraint. Penalizes scheds with some pilots working much more or less.
    Applies a penalty based on difference from the average.
    """

    def __init__(self, state: State):
        self._crew_hours: Dict[uuid.UUID, Tuple[Dict[str, datetime], float]] = {}
        self._total_minutes = 0.0
        self._state = state

    def each_event(self, gene: EventGene) -> None:
        """
        Called for each event in the individual.
        Track the earliest start and latest end.
        For each event, update the fitness with the overall change to the overage
        for that pilot's schedule, if any.
        """
        # for the pilot, save the earliest and latest times.
        event_start = self._state.events[gene.event_id].start
        event_end = self._state.events[gene.event_id].end
        if gene.pilot_id in self._crew_hours:
            old_start = self._crew_hours[gene.pilot_id][0]['start']
            old_end = self._crew_hours[gene.pilot_id][0]['end']
            start = old_start if old_start <= event_start else event_start
            end = old_end if old_end >= event_end else event_end
            old_work_minutes = (old_end - old_start).total_seconds() / 60
        else:
            start = event_start
            end = event_end
            old_work_minutes = 0.0

        # calculate work day
        new_work_minutes = (end - start).total_seconds() / 60

        # add any increase to the total
        # this avoids an extra loop at the end
        self._total_minutes += new_work_minutes - old_work_minutes

        # update the pilot hours data
        self._crew_hours[gene.pilot_id] = ({
            'start': start,
            'end': end,
        }, new_work_minutes)

    def get_final_fitness(self) -> float:
        """
        Return the fitness calculated with each_event().
        """
        fitness = 0.0
        # also penalizes unscheduled aircrew, this may conflict with sniv constraint fitness
        avg_minutes = self._total_minutes / len(self._state.pilots)
        for pilot_id in self._state.pilots:
            work_day = self._crew_hours[pilot_id][1] if pilot_id in self._crew_hours else 0
            fitness += abs(work_day - avg_minutes)
        return fitness * FAIR_HOURS_WEIGHT

    @property
    def indiv_is_feasible(self) -> bool:
        return True

    @property
    def is_hard_constraint(self) -> bool:
        return False

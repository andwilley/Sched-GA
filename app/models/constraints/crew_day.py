"""
Crew day Constraint
"""

from datetime import datetime, timedelta
from typing import Dict
import uuid
from app.models.constraints.constraint import Constraint
from app.models.event_gene import EventGene
from app.models.state import State
# these should be passed as a parameters:
from app.constants.opnav import DAY_CREW_DAY, NIGHT_CREW_DAY
from app.constants.environment import SUNSET
from app.ga.parameters import CREWDAY_WEIGHT

class CrewDay(Constraint):
    """
    CrewDay constraint. Limits pilots to DAY_CREW_DAY or NIGHT_CREW_DAY hours per day.
    Applies a penalty if an overage occurs.
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
        self._crew_hours: Dict[uuid.UUID, Dict[str, datetime]] = {}
        self._state = state

    def each_event(self, gene: EventGene) -> None:
        """
        Called for each event in the individual.
        Track the earliest start and latest end, as well as the penalty (fitness).
        For each event, update the fitness with the overall change to the overage
        for that pilot's schedule, if any.

        Args:
            gene: the EventGene to evaluate

        Returns:
            None
        """

        # for the pilot, save the earliest and latest times.
        event_start = self._state.events[gene.event_id].start
        event_end = self._state.events[gene.event_id].end
        if gene.pilot_id in self._crew_hours:
            old_start = self._crew_hours[gene.pilot_id]['start']
            old_end = self._crew_hours[gene.pilot_id]['end']
            old_overage = self.minutes_over_crew_day(old_start, old_end)
            start = old_start if old_start <= event_start else event_start
            end = old_end if old_end >= event_end else event_end
        else:
            start = event_start
            end = event_end
            old_overage = 0.0

        # calculate crew day overage
        new_overage = self.minutes_over_crew_day(start, end)

        # add the difference in minutes overage to the fitness
        # this avoids another loop at the end
        self._fitness += new_overage - old_overage

        # update the pilot crew day data
        self._crew_hours[gene.pilot_id] = {
            'start': start,
            'end': end,
        }

    def get_final_fitness(self) -> float:
        """
        Returns:
            The fitness calculated with all each_event() calls.
        """
        return self._fitness * self._fitness * CREWDAY_WEIGHT

    @staticmethod
    def minutes_over_crew_day(start: datetime, end: datetime) -> float:
        """
        Calculate to number of minutes over crew day given a start and end.
        Assumes only flight events end after sunset.

        Args:
            start: the start date and time
            end: the end date and time

        Returns:
            The number of minutes over crew day or 0.0.
        """

        diff: timedelta = end - start

        crew_day = DAY_CREW_DAY if end < SUNSET else NIGHT_CREW_DAY

        minutes_diff: float = (diff.total_seconds() / 60) - (crew_day * 60)
        return minutes_diff if minutes_diff > 0 else 0.0

    @property
    def indiv_is_feasible(self) -> bool:
        return True if self._fitness == 0.0 else False

    @property
    def is_hard_constraint(self) -> bool:
        return True

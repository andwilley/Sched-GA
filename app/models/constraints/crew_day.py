from datetime import datetime, timedelta
from typing import Dict
import uuid
from app.models.constraints.constraint import Constraint
from app.models.event_gene import EventGene
# from app.state.events import events
from app.test.test_state import events
from app.constants.opnav import DAY_CREW_DAY, NIGHT_CREW_DAY
from app.constants.environment import SUNSET

class CrewDay(Constraint):
    """
    CrewDay constraint. Limits pilots to DAY_CREW_DAY or NIGHT_CREW_DAY hours per day.
    Applies a penalty if an overage occurs.
    """

    def __init__(self):
        self._fitness = 0.0
        self._crew_hours: Dict[uuid.UUID, Dict[str, datetime]] = {}

    def each_event(self, gene: EventGene) -> None:
        """
        Called for each event in the individual.
        Track the earliest start and latest end, as well as the penalty (fitness).
        For each event, update the fitness with the overall change to the overage
        for that pilot's schedule, if any.
        """
        # for the pilot, save the earliest and latest times.
        event_start = events[gene.event_id].start
        event_end = events[gene.event_id].end
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

    def get_final_fitness(self) -> int:
        """
        Return the fitness calculated with each_event().
        """
        return int(self._fitness)

    @staticmethod
    def minutes_over_crew_day(start: datetime, end: datetime) -> float:
        diff: timedelta = end - start
        minutes_diff: float = diff.total_seconds() / 60

        # assumes only flight events end after sunset
        crew_day = DAY_CREW_DAY if end < SUNSET else NIGHT_CREW_DAY
        return minutes_diff if minutes_diff - (crew_day * 60) > 0 else 0.0

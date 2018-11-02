from datetime import datetime
from typing import Dict
import uuid
from models.constraints.constraint import Constraint
from models.event_gene import EventGene
from app.state.pilots import pilots
from app.state.events import events

class CrewDay(Constraint):

    def __init__(self):
        self.fitness = 0
        self.crew_hours: Dict[uuid.UUID, Dict[str, datetime]] = {}

    def each_event(self, gene: EventGene) -> None:
        # for the pilot, save the earliest and latest times.
        event_start = events[gene.event_id].start
        event_end = events[gene.event_id].end
        if gene.pilot_id in self.crew_hours:
            old_start = self.crew_hours[gene.pilot_id]['start']
            old_end = self.crew_hours[gene.pilot_id]['end']
            start = old_start if old_start <= event_start else event_start
            end = old_end if old_end <= event_end else event_end
        else:
            start = event_start
            end = event_end
        self.crew_hours[gene.pilot_id] = {
            'start': start,
            'end': end,
        }

    def get_final_fitness(self) -> int:
        return self.fitness

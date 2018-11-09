import uuid
from typing import Dict, List
from app.models.pilot import Pilot
from app.models.event import Event
from app.models.event_gene import EventGene

class State():

    def __init__(self, pilots: Dict[uuid.UUID, Pilot], events: Dict[uuid.UUID, Event],
                 schedule: List[EventGene], alleles: Dict[uuid.UUID, List[uuid.UUID]]):
        self.pilots = pilots
        self.events = events
        self.schedule = schedule
        self.alleles = alleles

    @property
    def pilots(self) -> Dict[uuid.UUID, Pilot]:
        return self._pilots

    @pilots.setter
    def pilots(self, pilots: Dict[uuid.UUID, Pilot]) -> None:
        self._pilots = pilots

    @property
    def events(self) -> Dict[uuid.UUID, Event]:
        return self._events

    @events.setter
    def events(self, events: Dict[uuid.UUID, Event]) -> None:
        self._events = events

    @property
    def schedule(self) -> List[EventGene]:
        return self._schedule

    @schedule.setter
    def schedule(self, schedule: List[EventGene]) -> None:
        self._schedule = schedule

    @property
    def alleles(self) -> Dict[uuid.UUID, List[uuid.UUID]]:
        return self._alleles

    @alleles.setter
    def alleles(self, alleles: Dict[uuid.UUID, List[uuid.UUID]]) -> None:
        self._alleles = alleles

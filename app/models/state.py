import uuid
from typing import Dict, List, Tuple
from app.models.pilot import Pilot
from app.models.event import Event
from app.models.event_gene import EventGene

class State():

    def __init__(self, pilots: Dict[uuid.UUID, Pilot], events: Dict[uuid.UUID, Event]):
        self.pilots = pilots
        self.events = events
        self.schedule, self.alleles = self._build_sched_and_alleles()

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

    def _build_sched_and_alleles(self) -> Tuple[List[EventGene], Dict[uuid.UUID, List[uuid.UUID]]]:
        alleles: Dict[uuid.UUID, List[uuid.UUID]] = {}
        schedule: List[EventGene] = []
        for _, event in self.events.items():
            # for now, assign all pilots to each event
            # eventually this will manage availability and qual constraints
            # can use the constraint model and loop for each pilot on each event:
            # pass in the event in question first, then loop through the pilot's snivs
            # if fitness is greater than 0, ingore that pilot, otherwise add to the list
            #
            # qual is a quick compare of event required qual to pilot qual. constraint model
            # for consistency worth it?
            alleles[event.id] = [pilot_id for pilot_id in self.pilots]
            schedule.append(EventGene(event.id))
        return schedule, alleles

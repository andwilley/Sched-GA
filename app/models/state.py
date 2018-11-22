import uuid
from math import inf
from typing import Dict, List, Tuple
from app.models.pilot import Pilot
from app.models.event import Event
from app.models.sniv import Sniv
from app.models.event_gene import EventGene

class State():

    def __init__(self, pilots: Dict[uuid.UUID, Pilot], events: Dict[uuid.UUID, Event],
                 snivs: Dict[uuid.UUID, Sniv] = None):
        self.pilots = pilots
        self.events = events
        self.snivs = snivs if snivs else {}
        self.add_snivs_to_pilots() # this mutates self.pilots
        self.schedule, self.alleles = self._build_sched_and_alleles()
        self._normalize_odo() # this mutates self.pilots

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

    def add_snivs_to_pilots(self) -> None:
        for _, sniv in self.snivs.items():
            self.pilots[sniv.pilot_id].snivs.append(sniv.id)

    def _build_sched_and_alleles(self) -> Tuple[List[EventGene], Dict[uuid.UUID, List[uuid.UUID]]]:
        alleles: Dict[uuid.UUID, List[uuid.UUID]] = {}
        schedule: List[EventGene] = []
        for _, event in self.events.items():
            # for each pilot sniv, check against the event
            pilot_available: Dict[uuid.UUID, bool] = {}
            for _, pilot in self.pilots.items():
                pilot_available[pilot.id] = True
                for sniv_id in pilot.snivs:
                    pilot_available[pilot.id] = False if max(self.events[event.id].start,
                                                             self.snivs[sniv_id].start) < \
                                                         min(self.events[event.id].end,
                                                             self.snivs[sniv_id].end) \
                                                      else pilot_available[pilot.id]
            # put pilot_id in allele if has qual, is available and is a pilot if needs to be
            alleles[event.id] = [pilot_id for pilot_id in self.pilots \
                if (event.qual_req in self.pilots[pilot_id].quals and pilot_available[pilot_id]
                    and (self.pilots[pilot_id].plt or (not self.pilots[pilot_id].plt and
                                                       not self.events[event.id].plt_req)))]
            if not alleles[event.id]:
                raise ValueError("It looks like no one is available for event: {}".format(event.id))
            schedule.append(EventGene(event.id))
        return schedule, alleles

    def _normalize_odo(self) -> None:
        # mutates pilot
        max_days = 0
        min_days = 9999999
        for _, pilot in self.pilots.items():
            if pilot.last_odo < min_days:
                min_days = pilot.last_odo
            if pilot.last_odo > max_days:
                max_days = pilot.last_odo
        for _, pilot in self.pilots.items():
            pilot.last_odo_norm = (pilot.last_odo - min_days) / (max_days - min_days)

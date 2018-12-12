"""
The appication state model
"""

import uuid
from typing import Dict, List, Tuple
from app.models.pilot import Pilot
from app.models.event import Event
from app.models.sniv import Sniv
from app.models.event_gene import EventGene

class State():
    """
    Creates and stores the needed data-structures for use by the appliction. Responsible for
    creating the allele-based composite chromosome based on event times, qualifications and pilot
    qualifications and snivs.
    """

    def __init__(self, pilots: Dict[uuid.UUID, Pilot], events: Dict[uuid.UUID, Event],
                 snivs: Dict[uuid.UUID, Sniv] = None):
        """
        Creates the State object.

        Args:
            pilots: a dict of pilot objects representing every schedulable pilot
            events: a dict of events that need to be matched with pilots (the schedule)
            snivs: a dict of schedule requests

        Returns:
            None
        """

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
        """
        Creates the list of EventGenes from the passed schedule, creates the allele for each
        event by filtering out pilots that aren't qualified or aren't available.

        Returns:
            Tuple[0]: the list of EventGenes
            Tuple[1]: the list of alleles in order of events in the first index of this tuple.
        """

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
            # it's possible that no one is available to fill a specific event, can write this sched
            if not alleles[event.id]:
                raise ValueError("It looks like no one is available for event: {}".format(event.id))
            schedule.append(EventGene(event.id))
        return schedule, alleles

    def _normalize_odo(self) -> None:
        """
        Save a normalized value for days since last ODO in each pilot for use with the fair ODO
        constraint. Most days since last ODO mapped to 1, least to 0.
        Mutates the pilot object (last_odo_norm field).
        """

        max_days = 0
        # bad practice, got type error with math.inf since thats a float. In reality, no one can
        # be around long enough to have a value this high, it gets initialized to 0.
        min_days = 9999999
        # find the max and min days since last ODO
        for _, pilot in self.pilots.items():
            if pilot.last_odo < min_days:
                min_days = pilot.last_odo
            if pilot.last_odo > max_days:
                max_days = pilot.last_odo
        # use max and min days to normalize ODO
        max_minus_min = max_days - min_days
        if max_minus_min < 1:
            max_minus_min = 1
        for _, pilot in self.pilots.items():
            pilot.last_odo_norm = (pilot.last_odo - min_days) / max_minus_min

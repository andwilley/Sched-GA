import uuid
from typing import Dict
from datetime import datetime
from app.models.event import Event
from app.models.pilot import Pilot
from app.models.event_gene import EventGene
from app.constants.quals import TRANS
from app.constants.event_types import FLIGHT, ODO

# avg = 3 hours, 2 hours penalty for 1 and 3
event1 = Event(datetime(2019, 1, 1, 6, 0), datetime(2019, 1, 1, 7, 0), ODO, TRANS)
event2 = Event(datetime(2019, 1, 1, 10, 0), datetime(2019, 1, 1, 13, 0), FLIGHT, TRANS)
event3 = Event(datetime(2019, 1, 1, 10, 0), datetime(2019, 1, 1, 15, 0), FLIGHT, TRANS)

events: Dict[uuid.UUID, Event] = {
    event1.id: event1,
    event2.id: event2,
    event3.id: event3,
}

# 3 pilots
pilot1 = Pilot("Dump", [TRANS], last_odo=0)
pilot2 = Pilot("Steam", [TRANS], last_odo=5)
pilot3 = Pilot("Space", [TRANS], last_odo=10)

pilots = {
    pilot1.id: pilot1,
    pilot2.id: pilot2,
    pilot3.id: pilot3,
}

# make event genes, wrong ODO
gene1 = EventGene(event1.id)
gene1.pilot_id = pilot1.id

gene2 = EventGene(event2.id)
gene2.pilot_id = pilot2.id

gene3 = EventGene(event3.id)
gene3.pilot_id = pilot3.id

# second set, right ODO
gene4 = EventGene(event1.id)
gene4.pilot_id = pilot3.id

gene5 = EventGene(event2.id)
gene5.pilot_id = pilot2.id

gene6 = EventGene(event3.id)
gene6.pilot_id = pilot1.id

# make individual
indiv1 = [gene1, gene2, gene3]
indiv2 = [gene4, gene5, gene6]

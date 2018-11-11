import uuid
from typing import Dict
from datetime import datetime
from app.models.event import Event
from app.models.pilot import Pilot
from app.models.event_gene import EventGene

# avg = 3 hours, 2 hours penalty for 1 and 3
event1 = Event(datetime(2019, 1, 1, 6, 0), datetime(2019, 1, 1, 7, 0), "flight")
event2 = Event(datetime(2019, 1, 1, 10, 0), datetime(2019, 1, 1, 13, 0), "flight")
event3 = Event(datetime(2019, 1, 1, 10, 0), datetime(2019, 1, 1, 15, 0), "flight")

# avg = 3 hours, no penalties
event4 = Event(datetime(2019, 1, 1, 6, 0), datetime(2019, 1, 1, 9, 0), "flight")
event5 = Event(datetime(2019, 1, 1, 10, 0), datetime(2019, 1, 1, 13, 0), "flight")
event6 = Event(datetime(2019, 1, 1, 10, 0), datetime(2019, 1, 1, 13, 0), "flight")

events: Dict[uuid.UUID, Event] = {
    event1.id: event1,
    event2.id: event2,
    event3.id: event3,
    event4.id: event4,
    event5.id: event5,
    event6.id: event6,
}

# 3 pilots
pilot1 = Pilot("Dump")
pilot2 = Pilot("Steam")
pilot3 = Pilot("Space")

pilots = {
    pilot1.id: pilot1,
    pilot2.id: pilot2,
    pilot3.id: pilot3,
}

# make event genes
gene1 = EventGene(event1.id)
gene1.pilot_id = pilot1.id

gene2 = EventGene(event2.id)
gene2.pilot_id = pilot2.id

gene3 = EventGene(event3.id)
gene3.pilot_id = pilot3.id

gene4 = EventGene(event4.id)
gene4.pilot_id = pilot1.id

gene5 = EventGene(event5.id)
gene5.pilot_id = pilot2.id

gene6 = EventGene(event6.id)
gene6.pilot_id = pilot3.id

# make individual
indiv1 = [gene1, gene2, gene3]
indiv2 = [gene4, gene5, gene6]

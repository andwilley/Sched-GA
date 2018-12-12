"""
Crew Day test state (x)
"""

import uuid
from typing import Dict
from datetime import datetime
from app.models.event import Event
from app.models.pilot import Pilot
from app.models.event_gene import EventGene
from app.constants.quals import TRANS

# violates day crew day by 1 hour
event1 = Event(datetime(2019, 1, 1, 6, 0), datetime(2019, 1, 1, 7, 0), "flight", TRANS)
event2 = Event(datetime(2019, 1, 1, 18, 0), datetime(2019, 1, 1, 19, 0), "flight", TRANS)

# violates night crew day by 2 hours
event3 = Event(datetime(2019, 1, 1, 10, 0), datetime(2019, 1, 1, 11, 0), "flight", TRANS)
event4 = Event(datetime(2019, 1, 1, 21, 0), datetime(2019, 1, 1, 22, 0), "flight", TRANS)

# does not violate crew day
event5 = Event(datetime(2019, 1, 1, 10, 0), datetime(2019, 1, 1, 11, 0), "flight", TRANS)
event6 = Event(datetime(2019, 1, 1, 12, 0), datetime(2019, 1, 1, 13, 0), "flight", TRANS)

# total violation 180 minutes ( 3 hours )

events: Dict[uuid.UUID, Event] = {
    event1.id: event1,
    event2.id: event2,
    event3.id: event3,
    event4.id: event4,
    event5.id: event5,
}

# 3 pilots
pilot1 = Pilot("Steam", [TRANS])
pilot2 = Pilot("Beef", [TRANS])
pilot3 = Pilot("Cox", [TRANS])

cd_pilots = {
    pilot1.id: pilot1,
    pilot2.id: pilot2,
    pilot3.id: pilot3,
}

# make event genes
gene1 = EventGene(event1.id)
gene1.pilot_id = pilot1.id

gene2 = EventGene(event2.id)
gene2.pilot_id = pilot1.id

gene3 = EventGene(event3.id)
gene3.pilot_id = pilot2.id

gene4 = EventGene(event4.id)
gene4.pilot_id = pilot2.id

gene5 = EventGene(event5.id)
gene5.pilot_id = pilot3.id

# make individual
indiv_crewday = [gene1, gene2, gene3, gene4, gene5]
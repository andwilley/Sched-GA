import uuid
from typing import Dict
from datetime import datetime
from app.models.event import Event
from app.models.pilot import Pilot
from app.models.event_gene import EventGene

"""
Crew Day test state
"""

# violates day crew day by 1 hour
event1 = Event(datetime(2019, 1, 1, 6, 0), datetime(2019, 1, 1, 7, 0), "flight")
event2 = Event(datetime(2019, 1, 1, 18, 0), datetime(2019, 1, 1, 19, 0), "flight")

# violates night crew day by 2 hours
event3 = Event(datetime(2019, 1, 1, 10, 0), datetime(2019, 1, 1, 11, 0), "flight")
event4 = Event(datetime(2019, 1, 1, 21, 0), datetime(2019, 1, 1, 22, 0), "flight")

# does not violate crew day
event5 = Event(datetime(2019, 1, 1, 10, 0), datetime(2019, 1, 1, 11, 0), "flight")
event6 = Event(datetime(2019, 1, 1, 12, 0), datetime(2019, 1, 1, 13, 0), "flight")

events: Dict[uuid.UUID, Event] = {
    event1.id: event1,
    event2.id: event2,
    event3.id: event3,
    event4.id: event4,
    event5.id: event5,
    event6.id: event6,
}

# 3 pilots
pilot1 = Pilot()
pilot2 = Pilot()
pilot3 = Pilot()

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

gene6 = EventGene(event6.id)
gene6.pilot_id = pilot3.id

# make individual
indiv = [gene1, gene2, gene3, gene4, gene5, gene6]

"""
operators test state
"""

# event ids
uuid1 = uuid.UUID('00000000-0000-0000-0000-000000000001')
uuid2 = uuid.UUID('00000000-0000-0000-0000-000000000002')
uuid3 = uuid.UUID('00000000-0000-0000-0000-000000000003')

# pilot ids
uuid11 = uuid.UUID('00000000-0000-0000-0000-000000000011')
uuid12 = uuid.UUID('00000000-0000-0000-0000-000000000012')
uuid13 = uuid.UUID('00000000-0000-0000-0000-000000000013')
uuid14 = uuid.UUID('00000000-0000-0000-0000-000000000014')
uuid15 = uuid.UUID('00000000-0000-0000-0000-000000000015')
uuid16 = uuid.UUID('00000000-0000-0000-0000-000000000016')
uuid17 = uuid.UUID('00000000-0000-0000-0000-000000000017')
uuid18 = uuid.UUID('00000000-0000-0000-0000-000000000018')
uuid19 = uuid.UUID('00000000-0000-0000-0000-000000000019')

schedule = [EventGene(uuid1), EventGene(uuid2), EventGene(uuid3)]

sched_alleles = {
    uuid1: [uuid11, uuid12, uuid13],
    uuid2: [uuid14, uuid15, uuid16],
    uuid3: [uuid17, uuid18, uuid19],
}
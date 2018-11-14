import uuid
from typing import Dict
from datetime import datetime
from app.models.pilot import Pilot
from app.models.sniv import Sniv
from app.models.event import Event
from app.constants.quals import STK, A2A, CQ

event1 = Event(datetime(2019, 1, 1, 7, 0), datetime(2019, 1, 1, 9, 0), "flight", STK)
event2 = Event(datetime(2019, 1, 1, 10, 0), datetime(2019, 1, 1, 11, 0), "flight", STK)
event3 = Event(datetime(2019, 1, 1, 14, 0), datetime(2019, 1, 1, 15, 0), "flight", A2A)
event4 = Event(datetime(2019, 1, 1, 21, 0), datetime(2019, 1, 1, 22, 0), "flight", CQ)
event5 = Event(datetime(2019, 1, 1, 21, 0), datetime(2019, 1, 1, 22, 0), "flight", A2A)

events1: Dict[uuid.UUID, Event] = {
    event1.id: event1,
    event2.id: event2,
    event3.id: event3,
    event4.id: event4,
}

events2: Dict[uuid.UUID, Event] = {
    event1.id: event1,
    event2.id: event2,
    event3.id: event3,
    event5.id: event5,
}


pilot1 = Pilot("Steam", [STK])
pilot2 = Pilot("Virgil", [A2A])
pilot3 = Pilot("Dump", [STK, A2A])
pilot7 = Pilot("Space", [CQ])
pilot8 = Pilot("Tummy", [CQ])

pilots1 = {
    pilot1.id: pilot1,
    pilot2.id: pilot2,
    pilot3.id: pilot3,
    pilot7.id: pilot7,
    pilot8.id: pilot8,
}

pilots2 = {
    pilot1.id: pilot1,
    pilot2.id: pilot2,
    pilot3.id: pilot3,
    pilot8.id: pilot8,
}


sniv1 = Sniv(datetime(2019, 1, 1, 8, 0), datetime(2019, 1, 1, 9, 0), pilot1.id, 'dental')
sniv2 = Sniv(datetime(2019, 1, 1, 20, 0), datetime(2019, 1, 1, 23, 0), pilot8.id, 'dental')

snivs = {
    sniv1.id: sniv1,
    sniv2.id: sniv2,
}

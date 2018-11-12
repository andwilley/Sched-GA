import uuid
from typing import Dict
from datetime import datetime
from app.models.event import Event
from app.constants.quals import TRANS, STK, A2A, CQ

event1 = Event(datetime(2019, 1, 1, 7, 0), datetime(2019, 1, 1, 9, 0), "flight", TRANS)
event2 = Event(datetime(2019, 1, 1, 7, 0), datetime(2019, 1, 1, 9, 0), "flight", TRANS)
event3 = Event(datetime(2019, 1, 1, 10, 0), datetime(2019, 1, 1, 11, 0), "flight", STK)
event4 = Event(datetime(2019, 1, 1, 10, 0), datetime(2019, 1, 1, 11, 0), "flight", STK)
event5 = Event(datetime(2019, 1, 1, 15, 0), datetime(2019, 1, 1, 16, 0), "flight", STK)
event6 = Event(datetime(2019, 1, 1, 15, 0), datetime(2019, 1, 1, 16, 0), "flight", STK)
event7 = Event(datetime(2019, 1, 1, 18, 0), datetime(2019, 1, 1, 19, 0), "flight", A2A)
event8 = Event(datetime(2019, 1, 1, 18, 0), datetime(2019, 1, 1, 19, 0), "flight", A2A)
event9 = Event(datetime(2019, 1, 1, 21, 0), datetime(2019, 1, 1, 22, 0), "flight", TRANS)
event10 = Event(datetime(2019, 1, 1, 21, 0), datetime(2019, 1, 1, 22, 0), "flight", CQ)

# event11 = Event(datetime(2019, 1, 1, 8, 0), datetime(2019, 1, 1, 9, 15), "flight")
# event12 = Event(datetime(2019, 1, 1, 8, 0), datetime(2019, 1, 1, 9, 15), "flight")
# event13 = Event(datetime(2019, 1, 1, 8, 0), datetime(2019, 1, 1, 10, 0), "flight")
# event14 = Event(datetime(2019, 1, 1, 10, 0), datetime(2019, 1, 1, 12, 0), "flight")
# event15 = Event(datetime(2019, 1, 1, 13, 0), datetime(2019, 1, 1, 14, 30), "flight")
# event16 = Event(datetime(2019, 1, 1, 13, 0), datetime(2019, 1, 1, 14, 30), "flight")

events: Dict[uuid.UUID, Event] = {
    event1.id: event1,
    event2.id: event2,
    event3.id: event3,
    event4.id: event4,
    event5.id: event5,
    event6.id: event6,
    event7.id: event7,
    event8.id: event8,
    event9.id: event9,
    event10.id: event10,

    # event11.id: event11,
    # event12.id: event12,
    # event13.id: event13,
    # event14.id: event14,
    # event15.id: event15,
    # event16.id: event16,
}
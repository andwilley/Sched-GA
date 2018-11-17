import uuid
from typing import Dict
from datetime import datetime
from app.models.event import Event
from app.constants.quals import TRANS, STK, A2A, CQ
from app.constants.event_types import FLIGHT, SIM, ODO

event1 = Event(datetime(2019, 1, 1, 7, 0), datetime(2019, 1, 1, 9, 0), ODO, TRANS)
event2 = Event(datetime(2019, 1, 1, 7, 0), datetime(2019, 1, 1, 9, 0), FLIGHT, TRANS)
event3 = Event(datetime(2019, 1, 1, 10, 0), datetime(2019, 1, 1, 11, 0), SIM, STK)
event4 = Event(datetime(2019, 1, 1, 10, 0), datetime(2019, 1, 1, 11, 0), FLIGHT, STK)
event5 = Event(datetime(2019, 1, 1, 15, 0), datetime(2019, 1, 1, 16, 0), ODO, STK)
event6 = Event(datetime(2019, 1, 1, 15, 0), datetime(2019, 1, 1, 16, 0), FLIGHT, STK)
event7 = Event(datetime(2019, 1, 1, 18, 0), datetime(2019, 1, 1, 19, 0), SIM, A2A)
event8 = Event(datetime(2019, 1, 1, 18, 0), datetime(2019, 1, 1, 19, 0), FLIGHT, A2A)
event9 = Event(datetime(2019, 1, 1, 21, 0), datetime(2019, 1, 1, 22, 0), ODO, TRANS)
event10 = Event(datetime(2019, 1, 1, 21, 0), datetime(2019, 1, 1, 22, 0), FLIGHT, CQ)

# event11 = Event(datetime(2019, 1, 1, 8, 0), datetime(2019, 1, 1, 9, 15), FLIGHT)
# event12 = Event(datetime(2019, 1, 1, 8, 0), datetime(2019, 1, 1, 9, 15), FLIGHT)
# event13 = Event(datetime(2019, 1, 1, 8, 0), datetime(2019, 1, 1, 10, 0), FLIGHT)
# event14 = Event(datetime(2019, 1, 1, 10, 0), datetime(2019, 1, 1, 12, 0), FLIGHT)
# event15 = Event(datetime(2019, 1, 1, 13, 0), datetime(2019, 1, 1, 14, 30), FLIGHT)
# event16 = Event(datetime(2019, 1, 1, 13, 0), datetime(2019, 1, 1, 14, 30), FLIGHT)

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
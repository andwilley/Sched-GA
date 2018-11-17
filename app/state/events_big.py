import uuid
from typing import Dict
from datetime import datetime
from app.models.event import Event
import app.constants.quals as qls
from app.constants.event_types import FLIGHT, SIM, ODO

event1 = Event(datetime(2019, 1, 1, 7, 0), datetime(2019, 1, 1, 9, 0), ODO, qls.TRANS)
event2 = Event(datetime(2019, 1, 1, 7, 0), datetime(2019, 1, 1, 9, 0), FLIGHT, qls.TRANS)
event3 = Event(datetime(2019, 1, 1, 10, 0), datetime(2019, 1, 1, 11, 0), SIM, qls.STK)
event4 = Event(datetime(2019, 1, 1, 10, 0), datetime(2019, 1, 1, 11, 0), FLIGHT, qls.STK)
event5 = Event(datetime(2019, 1, 1, 15, 0), datetime(2019, 1, 1, 16, 0), ODO, qls.STK)
event6 = Event(datetime(2019, 1, 1, 15, 0), datetime(2019, 1, 1, 16, 0), FLIGHT, qls.STK)
event7 = Event(datetime(2019, 1, 1, 18, 0), datetime(2019, 1, 1, 19, 0), SIM, qls.FWT1)
event8 = Event(datetime(2019, 1, 1, 18, 0), datetime(2019, 1, 1, 19, 0), FLIGHT, qls.FWT1)
event9 = Event(datetime(2019, 1, 1, 21, 0), datetime(2019, 1, 1, 22, 0), ODO, qls.TRANS)
event10 = Event(datetime(2019, 1, 1, 21, 0), datetime(2019, 1, 1, 22, 0), FLIGHT, qls.CQ)

"""
ODO 0645-1015 WSO
ODO 1015-1345 WSO
ODO 1345-1700 WSO
ODO 1700-2015 WSO

FCF 0800-1200
FCF 1200-1600

1800-2000 CQ (LSO)

flights:
0645-1000 FACA
0645-1000 FACA WSO
0645-1000 STK
0645-1000 TRANS
0645-1000 TRANS
700-1000 BFM
700-1000 BFM
700-1000 BFM
700-1000 BFM
0845-1200 BFM
0845-1200 BFM
0845-1200 BFM
0845-1200 STK
0845-1200 STK WSO
0845-1215 TRANS
1200-1515 FWT1
1200-1515 FWT1 WSO
1215-1515 BFM
1215-1515 BFM
1245-1600 STK
1245-1600 CAS
1415-1745 TRANS
1415-1745 TRANS
1645-2000 TRANS
1645-2000 TRANS
1645-2000 TRANS
1700-2000 NS
1700-2000 TRANS

0800-1230 WEEN
1400-1630 WEEN
1400-1630 FACA WSO

sims:
1330-1530 FWT2

classes:
0900-1200 TRANS
0930-1200 STK
1400-1500 NS
"""

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
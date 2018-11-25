from typing import List
from datetime import datetime
from app.models.event import Event
import app.constants.quals as qls
from app.constants.event_types import FLIGHT, SIM, ODO, CLS, LSO

_event_list: List[Event] = [
    # based on 17 oct 18

    # ODO 0645-1015 WSO
    Event(datetime(2019, 1, 1, 6, 45), datetime(2019, 1, 1, 10, 15), ODO, qls.ODO, False),
    # ODO 1015-1345 WSO
    Event(datetime(2019, 1, 1, 10, 15), datetime(2019, 1, 1, 13, 45), ODO, qls.ODO, False),
    # ODO 1345-1700 WSO
    Event(datetime(2019, 1, 1, 13, 45), datetime(2019, 1, 1, 17, 0), ODO, qls.ODO, False),
    # ODO 1700-2015 WSO
    Event(datetime(2019, 1, 1, 17, 0), datetime(2019, 1, 1, 20, 15), ODO, qls.ODO, False),

    # FCF 0800-1200
    Event(datetime(2019, 1, 1, 8, 0), datetime(2019, 1, 1, 12, 0), FLIGHT, qls.FCF),
    # FCF 1200-1600
    Event(datetime(2019, 1, 1, 12, 0), datetime(2019, 1, 1, 16, 0), FLIGHT, qls.FCF),
    # 1800-2000 CQ (LSO)
    Event(datetime(2019, 1, 1, 18, 0), datetime(2019, 1, 1, 20, 0), LSO, qls.CQ),

    # flights:
    # 0645-1000 FACA
    Event(datetime(2019, 1, 1, 6, 15), datetime(2019, 1, 1, 10, 30), FLIGHT, qls.FACA),
    # 0645-1000 FACA WSO
    Event(datetime(2019, 1, 1, 6, 15), datetime(2019, 1, 1, 10, 30), FLIGHT, qls.FACA, False),
    # 0645-1000 STK
    Event(datetime(2019, 1, 1, 6, 15), datetime(2019, 1, 1, 10, 30), FLIGHT, qls.STK),
    # 0645-1000 TRANS
    Event(datetime(2019, 1, 1, 6, 15), datetime(2019, 1, 1, 10, 30), FLIGHT, qls.TRANS),
    # 0645-1000 TRANS
    Event(datetime(2019, 1, 1, 6, 15), datetime(2019, 1, 1, 10, 30), FLIGHT, qls.TRANS),
    # 700-1000 BFM
    Event(datetime(2019, 1, 1, 6, 30), datetime(2019, 1, 1, 10, 30), FLIGHT, qls.BFM),
    # 700-1000 BFM
    Event(datetime(2019, 1, 1, 6, 30), datetime(2019, 1, 1, 10, 30), FLIGHT, qls.BFM),
    # 700-1000 BFM
    Event(datetime(2019, 1, 1, 6, 30), datetime(2019, 1, 1, 10, 30), FLIGHT, qls.BFM),
    # 700-1000 BFM
    Event(datetime(2019, 1, 1, 6, 30), datetime(2019, 1, 1, 10, 30), FLIGHT, qls.BFM),

    # 0845-1200 BFM
    Event(datetime(2019, 1, 1, 8, 15), datetime(2019, 1, 1, 12, 30), FLIGHT, qls.BFM),
    # 0845-1200 BFM
    Event(datetime(2019, 1, 1, 8, 15), datetime(2019, 1, 1, 12, 30), FLIGHT, qls.BFM),
    # 0845-1200 BFM
    Event(datetime(2019, 1, 1, 8, 15), datetime(2019, 1, 1, 12, 30), FLIGHT, qls.BFM),
    # 0845-1200 STK
    Event(datetime(2019, 1, 1, 8, 15), datetime(2019, 1, 1, 12, 30), FLIGHT, qls.STK),
    # 0845-1200 STK WSO
    Event(datetime(2019, 1, 1, 8, 15), datetime(2019, 1, 1, 12, 30), FLIGHT, qls.STK, False),
    # 0845-1215 TRANS
    Event(datetime(2019, 1, 1, 8, 15), datetime(2019, 1, 1, 12, 30), FLIGHT, qls.TRANS),

    # 1200-1515 FWT1
    Event(datetime(2019, 1, 1, 11, 30), datetime(2019, 1, 1, 15, 45), FLIGHT, qls.FWT1),
    # 1200-1515 FWT1 WSO
    Event(datetime(2019, 1, 1, 11, 30), datetime(2019, 1, 1, 15, 45), FLIGHT, qls.FWT1, False),
    # 1215-1515 BFM
    Event(datetime(2019, 1, 1, 11, 45), datetime(2019, 1, 1, 15, 45), FLIGHT, qls.BFM),
    # 1215-1515 BFM
    Event(datetime(2019, 1, 1, 11, 45), datetime(2019, 1, 1, 15, 45), FLIGHT, qls.BFM),
    # 1245-1600 STK
    Event(datetime(2019, 1, 1, 12, 15), datetime(2019, 1, 1, 16, 30), FLIGHT, qls.STK),
    # 1245-1600 CAS
    Event(datetime(2019, 1, 1, 12, 15), datetime(2019, 1, 1, 16, 30), FLIGHT, qls.CAS),

    # 1415-1745 TRANS
    Event(datetime(2019, 1, 1, 13, 45), datetime(2019, 1, 1, 18, 15), FLIGHT, qls.TRANS),
    # 1415-1745 TRANS
    Event(datetime(2019, 1, 1, 13, 45), datetime(2019, 1, 1, 18, 15), FLIGHT, qls.TRANS),

    # 1645-2000 TRANS
    Event(datetime(2019, 1, 1, 16, 15), datetime(2019, 1, 1, 20, 30), FLIGHT, qls.TRANS),
    # 1645-2000 TRANS
    Event(datetime(2019, 1, 1, 16, 15), datetime(2019, 1, 1, 20, 30), FLIGHT, qls.TRANS),
    # 1645-2000 TRANS
    Event(datetime(2019, 1, 1, 16, 15), datetime(2019, 1, 1, 20, 30), FLIGHT, qls.TRANS),
    # 1700-2000 NS
    Event(datetime(2019, 1, 1, 16, 30), datetime(2019, 1, 1, 20, 30), FLIGHT, qls.NS),
    # 1700-2000 TRANS
    Event(datetime(2019, 1, 1, 16, 30), datetime(2019, 1, 1, 20, 30), FLIGHT, qls.TRANS),

    # 0800-1230 WEEN
    Event(datetime(2019, 1, 1, 8, 00), datetime(2019, 1, 1, 12, 30), FLIGHT, qls.WEEN),
    # 1400-1630 WEEN
    Event(datetime(2019, 1, 1, 14, 00), datetime(2019, 1, 1, 16, 30), FLIGHT, qls.WEEN),
    # 1400-1630 FACA WSO
    Event(datetime(2019, 1, 1, 14, 00), datetime(2019, 1, 1, 16, 30), FLIGHT, qls.FACA, False),

    # sims:
    # 1330-1530 FWT2
    Event(datetime(2019, 1, 1, 13, 00), datetime(2019, 1, 1, 16, 00), SIM, qls.FWT2),

    # classes:
    # 0900-1200 TRANS
    Event(datetime(2019, 1, 1, 9, 00), datetime(2019, 1, 1, 12, 00), CLS, qls.TRANS, False),
    # 0930-1200 STK
    Event(datetime(2019, 1, 1, 9, 30), datetime(2019, 1, 1, 12, 00), CLS, qls.STK, False),
    # 1400-1500 NS
    Event(datetime(2019, 1, 1, 14, 00), datetime(2019, 1, 1, 15, 00), CLS, qls.NS, False),
]

events = {event.id: event for event in _event_list}

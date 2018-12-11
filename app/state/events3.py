from typing import List
from datetime import datetime
from app.models.event import Event
import app.constants.quals as qls
from app.constants.event_types import FLIGHT, SIM, ODO, CLS, LSO

_event_list: List[Event] = [
    # 38 events

    Event(datetime(2019, 1, 1, 6, 30), datetime(2019, 1, 1, 10, 0), ODO, qls.ODO, False),
    Event(datetime(2019, 1, 1, 10, 0), datetime(2019, 1, 1, 13, 0), ODO, qls.ODO, False),
    Event(datetime(2019, 1, 1, 13, 0), datetime(2019, 1, 1, 15, 30), ODO, qls.ODO, False),

    Event(datetime(2019, 1, 1, 8, 0), datetime(2019, 1, 1, 12, 0), FLIGHT, qls.FCF),
    Event(datetime(2019, 1, 1, 12, 0), datetime(2019, 1, 1, 16, 0), FLIGHT, qls.FCF),
    Event(datetime(2019, 1, 1, 15, 0), datetime(2019, 1, 1, 18, 0), LSO, qls.CQ),

    # flights:
    Event(datetime(2019, 1, 1, 6, 0), datetime(2019, 1, 1, 10, 0), FLIGHT, qls.FWT2),
    Event(datetime(2019, 1, 1, 6, 0), datetime(2019, 1, 1, 10, 30), FLIGHT, qls.TRANS),
    Event(datetime(2019, 1, 1, 6, 0), datetime(2019, 1, 1, 10, 30), FLIGHT, qls.TRANS),

    Event(datetime(2019, 1, 1, 7, 15), datetime(2019, 1, 1, 11, 30), FLIGHT, qls.FACA),
    Event(datetime(2019, 1, 1, 7, 15), datetime(2019, 1, 1, 11, 30), FLIGHT, qls.CAS),
    Event(datetime(2019, 1, 1, 7, 15), datetime(2019, 1, 1, 11, 30), FLIGHT, qls.FACA),
    Event(datetime(2019, 1, 1, 7, 15), datetime(2019, 1, 1, 11, 30), FLIGHT, qls.CAS),

    Event(datetime(2019, 1, 1, 8, 15), datetime(2019, 1, 1, 12, 45), FLIGHT, qls.TRANS),
    Event(datetime(2019, 1, 1, 8, 15), datetime(2019, 1, 1, 12, 45), FLIGHT, qls.TRANS),

    Event(datetime(2019, 1, 1, 10, 0), datetime(2019, 1, 1, 13, 0), FLIGHT, qls.BFM),
    Event(datetime(2019, 1, 1, 10, 0), datetime(2019, 1, 1, 13, 0), FLIGHT, qls.BFM),

    Event(datetime(2019, 1, 1, 10, 45), datetime(2019, 1, 1, 15, 15), FLIGHT, qls.TRANS),
    Event(datetime(2019, 1, 1, 10, 45), datetime(2019, 1, 1, 15, 15), FLIGHT, qls.TRANS),

    Event(datetime(2019, 1, 1, 12, 00), datetime(2019, 1, 1, 16, 00), FLIGHT, qls.BFM),
    Event(datetime(2019, 1, 1, 12, 00), datetime(2019, 1, 1, 16, 00), FLIGHT, qls.BFM),
    Event(datetime(2019, 1, 1, 12, 00), datetime(2019, 1, 1, 16, 00), FLIGHT, qls.BFM),

    # sims:
    Event(datetime(2019, 1, 1, 7, 0), datetime(2019, 1, 1, 11, 30), SIM, qls.TRANS, False),
    Event(datetime(2019, 1, 1, 7, 0), datetime(2019, 1, 1, 11, 30), SIM, qls.TRANS, False),
    Event(datetime(2019, 1, 1, 7, 0), datetime(2019, 1, 1, 11, 30), SIM, qls.NTPS),
    Event(datetime(2019, 1, 1, 10, 30), datetime(2019, 1, 1, 14, 30), SIM, qls.NS),
    Event(datetime(2019, 1, 1, 10, 30), datetime(2019, 1, 1, 13, 30), SIM, qls.NS),
    Event(datetime(2019, 1, 1, 12, 0), datetime(2019, 1, 1, 15, 30), SIM, qls.TRANS, False),


    # classes:
    Event(datetime(2019, 1, 1, 8, 00), datetime(2019, 1, 1, 9, 30), CLS, qls.TRANS, False),
    Event(datetime(2019, 1, 1, 8, 0), datetime(2019, 1, 1, 9, 30), CLS, qls.NS, False),
    Event(datetime(2019, 1, 1, 8, 30), datetime(2019, 1, 1, 9, 0), CLS, qls.TRANS, False),
    Event(datetime(2019, 1, 1, 9, 0), datetime(2019, 1, 1, 11, 0), CLS, qls.CAS, False),
    Event(datetime(2019, 1, 1, 9, 30), datetime(2019, 1, 1, 10, 30), CLS, qls.TRANS, False),
    Event(datetime(2019, 1, 1, 11, 0), datetime(2019, 1, 1, 13, 0), CLS, qls.CQ, False),
    Event(datetime(2019, 1, 1, 11, 0), datetime(2019, 1, 1, 13, 30), CLS, qls.FWT2, False),
    Event(datetime(2019, 1, 1, 12, 0), datetime(2019, 1, 1, 12, 30), CLS, qls.TRANS, False),
    Event(datetime(2019, 1, 1, 12, 30), datetime(2019, 1, 1, 14, 0), CLS, qls.TRANS, False),
    Event(datetime(2019, 1, 1, 14, 0), datetime(2019, 1, 1, 15, 0), CLS, qls.TRANS, False),
]

events = {event.id: event for event in _event_list}

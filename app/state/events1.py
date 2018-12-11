from typing import List
from datetime import datetime
from app.models.event import Event
import app.constants.quals as qls
from app.constants.event_types import FLIGHT, SIM, ODO, CLS, LSO

_event_list: List[Event] = [
    # 41 events

    # duties
    Event(datetime(2019, 1, 1, 6, 45), datetime(2019, 1, 1, 10, 15), ODO, qls.ODO, False),
    Event(datetime(2019, 1, 1, 10, 15), datetime(2019, 1, 1, 13, 45), ODO, qls.ODO, False),
    Event(datetime(2019, 1, 1, 13, 45), datetime(2019, 1, 1, 17, 0), ODO, qls.ODO, False),
    Event(datetime(2019, 1, 1, 17, 0), datetime(2019, 1, 1, 20, 15), ODO, qls.ODO, False),

    Event(datetime(2019, 1, 1, 8, 0), datetime(2019, 1, 1, 12, 0), FLIGHT, qls.FCF),
    Event(datetime(2019, 1, 1, 12, 0), datetime(2019, 1, 1, 16, 0), FLIGHT, qls.FCF),
    Event(datetime(2019, 1, 1, 18, 0), datetime(2019, 1, 1, 20, 0), LSO, qls.CQ),

    # flights
    Event(datetime(2019, 1, 1, 6, 15), datetime(2019, 1, 1, 10, 30), FLIGHT, qls.FACA),
    Event(datetime(2019, 1, 1, 6, 15), datetime(2019, 1, 1, 10, 30), FLIGHT, qls.FACA, False),
    Event(datetime(2019, 1, 1, 6, 15), datetime(2019, 1, 1, 10, 30), FLIGHT, qls.STK),
    Event(datetime(2019, 1, 1, 6, 15), datetime(2019, 1, 1, 10, 30), FLIGHT, qls.TRANS),
    Event(datetime(2019, 1, 1, 6, 15), datetime(2019, 1, 1, 10, 30), FLIGHT, qls.TRANS),
    Event(datetime(2019, 1, 1, 6, 30), datetime(2019, 1, 1, 10, 30), FLIGHT, qls.BFM),
    Event(datetime(2019, 1, 1, 6, 30), datetime(2019, 1, 1, 10, 30), FLIGHT, qls.BFM),
    Event(datetime(2019, 1, 1, 6, 30), datetime(2019, 1, 1, 10, 30), FLIGHT, qls.BFM),
    Event(datetime(2019, 1, 1, 6, 30), datetime(2019, 1, 1, 10, 30), FLIGHT, qls.BFM),

    Event(datetime(2019, 1, 1, 8, 15), datetime(2019, 1, 1, 12, 30), FLIGHT, qls.BFM),
    Event(datetime(2019, 1, 1, 8, 15), datetime(2019, 1, 1, 12, 30), FLIGHT, qls.BFM),
    Event(datetime(2019, 1, 1, 8, 15), datetime(2019, 1, 1, 12, 30), FLIGHT, qls.BFM),
    Event(datetime(2019, 1, 1, 8, 15), datetime(2019, 1, 1, 12, 30), FLIGHT, qls.STK),
    Event(datetime(2019, 1, 1, 8, 15), datetime(2019, 1, 1, 12, 30), FLIGHT, qls.STK, False),
    Event(datetime(2019, 1, 1, 8, 15), datetime(2019, 1, 1, 12, 30), FLIGHT, qls.TRANS),

    Event(datetime(2019, 1, 1, 11, 30), datetime(2019, 1, 1, 15, 45), FLIGHT, qls.FWT1),
    Event(datetime(2019, 1, 1, 11, 30), datetime(2019, 1, 1, 15, 45), FLIGHT, qls.FWT1, False),
    Event(datetime(2019, 1, 1, 11, 45), datetime(2019, 1, 1, 15, 45), FLIGHT, qls.BFM),
    Event(datetime(2019, 1, 1, 11, 45), datetime(2019, 1, 1, 15, 45), FLIGHT, qls.BFM),
    Event(datetime(2019, 1, 1, 12, 15), datetime(2019, 1, 1, 16, 30), FLIGHT, qls.STK),
    Event(datetime(2019, 1, 1, 12, 15), datetime(2019, 1, 1, 16, 30), FLIGHT, qls.CAS),

    Event(datetime(2019, 1, 1, 13, 45), datetime(2019, 1, 1, 18, 15), FLIGHT, qls.TRANS),
    Event(datetime(2019, 1, 1, 13, 45), datetime(2019, 1, 1, 18, 15), FLIGHT, qls.TRANS),

    Event(datetime(2019, 1, 1, 16, 15), datetime(2019, 1, 1, 20, 30), FLIGHT, qls.TRANS),
    Event(datetime(2019, 1, 1, 16, 15), datetime(2019, 1, 1, 20, 30), FLIGHT, qls.TRANS),
    Event(datetime(2019, 1, 1, 16, 15), datetime(2019, 1, 1, 20, 30), FLIGHT, qls.TRANS),
    Event(datetime(2019, 1, 1, 16, 30), datetime(2019, 1, 1, 20, 30), FLIGHT, qls.NS),
    Event(datetime(2019, 1, 1, 16, 30), datetime(2019, 1, 1, 20, 30), FLIGHT, qls.TRANS),

    Event(datetime(2019, 1, 1, 8, 00), datetime(2019, 1, 1, 12, 30), FLIGHT, qls.WEEN),
    Event(datetime(2019, 1, 1, 14, 00), datetime(2019, 1, 1, 16, 30), FLIGHT, qls.WEEN),
    Event(datetime(2019, 1, 1, 14, 00), datetime(2019, 1, 1, 16, 30), FLIGHT, qls.FACA, False),

    # sims:
    Event(datetime(2019, 1, 1, 13, 00), datetime(2019, 1, 1, 16, 00), SIM, qls.FWT2),

    # classes:
    Event(datetime(2019, 1, 1, 9, 00), datetime(2019, 1, 1, 12, 00), CLS, qls.TRANS, False),
    Event(datetime(2019, 1, 1, 9, 30), datetime(2019, 1, 1, 12, 00), CLS, qls.STK, False),
    Event(datetime(2019, 1, 1, 14, 00), datetime(2019, 1, 1, 15, 00), CLS, qls.NS, False),
]

events = {event.id: event for event in _event_list}

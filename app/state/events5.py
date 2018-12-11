from typing import List
from datetime import datetime
from app.models.event import Event
import app.constants.quals as qls
from app.constants.event_types import FLIGHT, SIM, ODO, CLS, LSO

_event_list: List[Event] = [
    # 44 events

    Event(datetime(2019, 1, 1, 6, 0), datetime(2019, 1, 1, 9, 30), ODO, qls.ODO, False),
    Event(datetime(2019, 1, 1, 9, 30), datetime(2019, 1, 1, 13, 0), ODO, qls.ODO, False),
    Event(datetime(2019, 1, 1, 13, 0), datetime(2019, 1, 1, 17, 0), ODO, qls.ODO, False),
    Event(datetime(2019, 1, 1, 17, 0), datetime(2019, 1, 1, 19, 45), ODO, qls.ODO, False),

    Event(datetime(2019, 1, 1, 8, 0), datetime(2019, 1, 1, 12, 0), FLIGHT, qls.FCF),
    Event(datetime(2019, 1, 1, 12, 0), datetime(2019, 1, 1, 16, 0), FLIGHT, qls.FCF),
    Event(datetime(2019, 1, 1, 15, 0), datetime(2019, 1, 1, 18, 0), LSO, qls.CQ),

    # flights:
    Event(datetime(2019, 1, 1, 5, 30), datetime(2019, 1, 1, 9, 30), FLIGHT, qls.BFM),
    Event(datetime(2019, 1, 1, 5, 30), datetime(2019, 1, 1, 9, 45), FLIGHT, qls.FWT1),
    Event(datetime(2019, 1, 1, 5, 30), datetime(2019, 1, 1, 9, 45), FLIGHT, qls.STK),

    Event(datetime(2019, 1, 1, 7, 30), datetime(2019, 1, 1, 11, 30), FLIGHT, qls.BFM),
    Event(datetime(2019, 1, 1, 7, 30), datetime(2019, 1, 1, 11, 45), FLIGHT, qls.FWT2),
    Event(datetime(2019, 1, 1, 7, 30), datetime(2019, 1, 1, 11, 45), FLIGHT, qls.FWT2),
    Event(datetime(2019, 1, 1, 7, 30), datetime(2019, 1, 1, 11, 45), FLIGHT, qls.CAS, False),
    Event(datetime(2019, 1, 1, 7, 30), datetime(2019, 1, 1, 12, 0), FLIGHT, qls.TRANS),
    Event(datetime(2019, 1, 1, 7, 30), datetime(2019, 1, 1, 12, 0), FLIGHT, qls.TRANS, False),

    Event(datetime(2019, 1, 1, 10, 30), datetime(2019, 1, 1, 14, 30), FLIGHT, qls.BFM),
    Event(datetime(2019, 1, 1, 10, 30), datetime(2019, 1, 1, 14, 30), FLIGHT, qls.BFM),
    Event(datetime(2019, 1, 1, 10, 30), datetime(2019, 1, 1, 14, 30), FLIGHT, qls.BFM),
    Event(datetime(2019, 1, 1, 11, 0), datetime(2019, 1, 1, 15, 15), FLIGHT, qls.FWT2),
    Event(datetime(2019, 1, 1, 11, 0), datetime(2019, 1, 1, 15, 15), FLIGHT, qls.FWT2),
    Event(datetime(2019, 1, 1, 11, 15), datetime(2019, 1, 1, 15, 30), FLIGHT, qls.STK),
    Event(datetime(2019, 1, 1, 11, 15), datetime(2019, 1, 1, 15, 30), FLIGHT, qls.STK, False),

    Event(datetime(2019, 1, 1, 12, 15), datetime(2019, 1, 1, 16, 15), FLIGHT, qls.BFM),
    Event(datetime(2019, 1, 1, 12, 15), datetime(2019, 1, 1, 16, 15), FLIGHT, qls.BFM),
    Event(datetime(2019, 1, 1, 13, 15), datetime(2019, 1, 1, 17, 30), FLIGHT, qls.TRANS),
    Event(datetime(2019, 1, 1, 13, 15), datetime(2019, 1, 1, 17, 30), FLIGHT, qls.CAS),
    Event(datetime(2019, 1, 1, 13, 15), datetime(2019, 1, 1, 17, 30), FLIGHT, qls.TRANS),

    Event(datetime(2019, 1, 1, 15, 0), datetime(2019, 1, 1, 20, 0), FLIGHT, qls.IFR),

    Event(datetime(2019, 1, 1, 7, 30), datetime(2019, 1, 1, 11, 45), FLIGHT, qls.WEEN),
    Event(datetime(2019, 1, 1, 7, 30), datetime(2019, 1, 1, 11, 45), FLIGHT, qls.FACA, False),
    Event(datetime(2019, 1, 1, 12, 45), datetime(2019, 1, 1, 15, 0), FLIGHT, qls.WEEN),

    # sims:
    Event(datetime(2019, 1, 1, 7, 0), datetime(2019, 1, 1, 11, 30), SIM, qls.CAS, False),
    Event(datetime(2019, 1, 1, 7, 0), datetime(2019, 1, 1, 9, 30), SIM, qls.TRANS, False),
    Event(datetime(2019, 1, 1, 7, 0), datetime(2019, 1, 1, 10, 0), SIM, qls.CAS, False),
    Event(datetime(2019, 1, 1, 7, 0), datetime(2019, 1, 1, 10, 30), SIM, qls.CAS, False),
    Event(datetime(2019, 1, 1, 8, 30), datetime(2019, 1, 1, 12, 30), SIM, qls.TRANS, False),
    Event(datetime(2019, 1, 1, 10, 45), datetime(2019, 1, 1, 15, 15), SIM, qls.CAS, False),
    Event(datetime(2019, 1, 1, 10, 45), datetime(2019, 1, 1, 15, 15), SIM, qls.CAS, False),
    Event(datetime(2019, 1, 1, 10, 45), datetime(2019, 1, 1, 14, 15), SIM, qls.NTPS, False),
    Event(datetime(2019, 1, 1, 12, 15), datetime(2019, 1, 1, 15, 15), SIM, qls.CAS, False),
    Event(datetime(2019, 1, 1, 12, 15), datetime(2019, 1, 1, 14, 45), SIM, qls.TRANS, False),

    # classes:
    Event(datetime(2019, 1, 1, 11, 45), datetime(2019, 1, 1, 13, 15), CLS, qls.FACA, False),
    Event(datetime(2019, 1, 1, 12, 0), datetime(2019, 1, 1, 13, 30), CLS, qls.FACA, False),
    Event(datetime(2019, 1, 1, 14, 0), datetime(2019, 1, 1, 15, 30), CLS, qls.IFR, False),
]

events = {event.id: event for event in _event_list}

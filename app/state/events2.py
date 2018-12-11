from typing import List
from datetime import datetime
from app.models.event import Event
import app.constants.quals as qls
from app.constants.event_types import FLIGHT, SIM, ODO, CLS, LSO

_event_list: List[Event] = [
    # 50 events

    Event(datetime(2019, 1, 1, 9, 45), datetime(2019, 1, 1, 13, 0), ODO, qls.ODO, False),
    Event(datetime(2019, 1, 1, 13, 0), datetime(2019, 1, 1, 17, 30), ODO, qls.ODO, False),
    Event(datetime(2019, 1, 1, 17, 30), datetime(2019, 1, 1, 21, 0), ODO, qls.ODO, False),

    Event(datetime(2019, 1, 1, 8, 0), datetime(2019, 1, 1, 12, 0), FLIGHT, qls.FCF),
    Event(datetime(2019, 1, 1, 12, 0), datetime(2019, 1, 1, 16, 0), FLIGHT, qls.FCF),
    Event(datetime(2019, 1, 1, 18, 0), datetime(2019, 1, 1, 20, 0), LSO, qls.CQ),

    # flights:
    Event(datetime(2019, 1, 1, 9, 15), datetime(2019, 1, 1, 13, 30), FLIGHT, qls.TRANS),
    Event(datetime(2019, 1, 1, 9, 15), datetime(2019, 1, 1, 13, 30), FLIGHT, qls.TRANS),

    Event(datetime(2019, 1, 1, 11, 30), datetime(2019, 1, 1, 15, 45), FLIGHT, qls.TRANS),
    Event(datetime(2019, 1, 1, 11, 30), datetime(2019, 1, 1, 15, 45), FLIGHT, qls.TRANS),
    Event(datetime(2019, 1, 1, 11, 30), datetime(2019, 1, 1, 15, 45), FLIGHT, qls.STK),
    Event(datetime(2019, 1, 1, 11, 30), datetime(2019, 1, 1, 15, 45), FLIGHT, qls.STK),

    Event(datetime(2019, 1, 1, 13, 30), datetime(2019, 1, 1, 17, 45), FLIGHT, qls.STK),
    Event(datetime(2019, 1, 1, 13, 30), datetime(2019, 1, 1, 17, 45), FLIGHT, qls.STK),

    Event(datetime(2019, 1, 1, 14, 45), datetime(2019, 1, 1, 18, 15), FLIGHT, qls.FWT2),
    Event(datetime(2019, 1, 1, 14, 45), datetime(2019, 1, 1, 18, 15), FLIGHT, qls.FWT2),
    Event(datetime(2019, 1, 1, 14, 45), datetime(2019, 1, 1, 18, 15), FLIGHT, qls.TRANS),
    Event(datetime(2019, 1, 1, 14, 45), datetime(2019, 1, 1, 18, 15), FLIGHT, qls.TRANS),
    Event(datetime(2019, 1, 1, 14, 45), datetime(2019, 1, 1, 18, 15), FLIGHT, qls.BFM),
    Event(datetime(2019, 1, 1, 14, 45), datetime(2019, 1, 1, 18, 15), FLIGHT, qls.BFM),

    Event(datetime(2019, 1, 1, 14, 30), datetime(2019, 1, 1, 19, 30), FLIGHT, qls.TRANS),
    Event(datetime(2019, 1, 1, 14, 30), datetime(2019, 1, 1, 19, 30), FLIGHT, qls.TRANS),

    Event(datetime(2019, 1, 1, 15, 45), datetime(2019, 1, 1, 19, 45), FLIGHT, qls.FWT2),
    Event(datetime(2019, 1, 1, 15, 45), datetime(2019, 1, 1, 19, 45), FLIGHT, qls.FWT2),
    Event(datetime(2019, 1, 1, 15, 45), datetime(2019, 1, 1, 19, 45), FLIGHT, qls.TRANS),
    Event(datetime(2019, 1, 1, 15, 45), datetime(2019, 1, 1, 19, 45), FLIGHT, qls.TRANS),
    Event(datetime(2019, 1, 1, 15, 45), datetime(2019, 1, 1, 19, 45), FLIGHT, qls.BFM),
    Event(datetime(2019, 1, 1, 15, 45), datetime(2019, 1, 1, 19, 45), FLIGHT, qls.BFM),

    Event(datetime(2019, 1, 1, 16, 30), datetime(2019, 1, 1, 20, 45), FLIGHT, qls.FACA),
    Event(datetime(2019, 1, 1, 16, 30), datetime(2019, 1, 1, 20, 45), FLIGHT, qls.FACA, False),
    Event(datetime(2019, 1, 1, 16, 30), datetime(2019, 1, 1, 20, 45), FLIGHT, qls.CAS),

    Event(datetime(2019, 1, 1, 17, 30), datetime(2019, 1, 1, 21, 15), FLIGHT, qls.TRANS),
    Event(datetime(2019, 1, 1, 17, 30), datetime(2019, 1, 1, 21, 15), FLIGHT, qls.TRANS),
    Event(datetime(2019, 1, 1, 17, 30), datetime(2019, 1, 1, 21, 15), FLIGHT, qls.TRANS),
    Event(datetime(2019, 1, 1, 17, 30), datetime(2019, 1, 1, 21, 15), FLIGHT, qls.TRANS),

    Event(datetime(2019, 1, 1, 13, 15), datetime(2019, 1, 1, 17, 45), FLIGHT, qls.WEEN),
    Event(datetime(2019, 1, 1, 13, 15), datetime(2019, 1, 1, 17, 45), FLIGHT, qls.FACA, False),
    Event(datetime(2019, 1, 1, 13, 15), datetime(2019, 1, 1, 17, 45), FLIGHT, qls.WEEN),
    Event(datetime(2019, 1, 1, 13, 15), datetime(2019, 1, 1, 17, 45), FLIGHT, qls.FACA, False),

    # sims:
    Event(datetime(2019, 1, 1, 7, 00), datetime(2019, 1, 1, 10, 30), SIM, qls.FWT2),
    Event(datetime(2019, 1, 1, 7, 00), datetime(2019, 1, 1, 10, 30), SIM, qls.FWT2),
    Event(datetime(2019, 1, 1, 7, 00), datetime(2019, 1, 1, 10, 30), SIM, qls.FWT2),
    Event(datetime(2019, 1, 1, 7, 00), datetime(2019, 1, 1, 10, 30), SIM, qls.FWT1),
    Event(datetime(2019, 1, 1, 9, 30), datetime(2019, 1, 1, 13, 30), SIM, qls.CQ),
    Event(datetime(2019, 1, 1, 13, 30), datetime(2019, 1, 1, 15, 30), SIM, qls.NTPS),


    # classes:
    Event(datetime(2019, 1, 1, 8, 00), datetime(2019, 1, 1, 12, 30), CLS, qls.TRANS, False),
    Event(datetime(2019, 1, 1, 11, 0), datetime(2019, 1, 1, 13, 30), CLS, qls.CQ, False),
    Event(datetime(2019, 1, 1, 13, 0), datetime(2019, 1, 1, 14, 0), CLS, qls.STK, False),
    Event(datetime(2019, 1, 1, 13, 30), datetime(2019, 1, 1, 14, 30), CLS, qls.TRANS, False),
    Event(datetime(2019, 1, 1, 13, 30), datetime(2019, 1, 1, 16, 30), CLS, qls.FWT1, False),
    Event(datetime(2019, 1, 1, 14, 30), datetime(2019, 1, 1, 16, 30), CLS, qls.TRANS, False),
]

events = {event.id: event for event in _event_list}

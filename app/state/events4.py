from typing import List
from datetime import datetime
from app.models.event import Event
import app.constants.quals as qls
from app.constants.event_types import FLIGHT, SIM, ODO, CLS, LSO

_event_list: List[Event] = [
    # 58 events

    Event(datetime(2019, 1, 1, 5, 45), datetime(2019, 1, 1, 10, 0), ODO, qls.ODO, False),
    Event(datetime(2019, 1, 1, 10, 0), datetime(2019, 1, 1, 13, 30), ODO, qls.ODO, False),
    Event(datetime(2019, 1, 1, 13, 30), datetime(2019, 1, 1, 15, 45), ODO, qls.ODO, False),
    Event(datetime(2019, 1, 1, 15, 45), datetime(2019, 1, 1, 19, 30), ODO, qls.ODO, False),

    Event(datetime(2019, 1, 1, 8, 0), datetime(2019, 1, 1, 12, 0), FLIGHT, qls.FCF),
    Event(datetime(2019, 1, 1, 12, 0), datetime(2019, 1, 1, 16, 0), FLIGHT, qls.FCF),
    Event(datetime(2019, 1, 1, 15, 0), datetime(2019, 1, 1, 18, 0), LSO, qls.CQ),

    # flights:
    Event(datetime(2019, 1, 1, 5, 15), datetime(2019, 1, 1, 9, 30), FLIGHT, qls.STK),
    Event(datetime(2019, 1, 1, 5, 30), datetime(2019, 1, 1, 9, 45), FLIGHT, qls.TRANS),
    Event(datetime(2019, 1, 1, 5, 30), datetime(2019, 1, 1, 9, 45), FLIGHT, qls.TRANS),
    Event(datetime(2019, 1, 1, 5, 30), datetime(2019, 1, 1, 9, 30), FLIGHT, qls.BFM),
    Event(datetime(2019, 1, 1, 6, 0), datetime(2019, 1, 1, 10, 0), FLIGHT, qls.BFM),
    Event(datetime(2019, 1, 1, 6, 0), datetime(2019, 1, 1, 10, 0), FLIGHT, qls.BFM),

    Event(datetime(2019, 1, 1, 7, 15), datetime(2019, 1, 1, 11, 15), FLIGHT, qls.BFM),
    Event(datetime(2019, 1, 1, 7, 15), datetime(2019, 1, 1, 11, 30), FLIGHT, qls.CAS, False),
    Event(datetime(2019, 1, 1, 7, 15), datetime(2019, 1, 1, 11, 45), FLIGHT, qls.CAS, False),
    Event(datetime(2019, 1, 1, 7, 30), datetime(2019, 1, 1, 12, 0), FLIGHT, qls.TRANS),
    Event(datetime(2019, 1, 1, 7, 30), datetime(2019, 1, 1, 12, 0), FLIGHT, qls.TRANS),
    Event(datetime(2019, 1, 1, 7, 45), datetime(2019, 1, 1, 11, 45), FLIGHT, qls.BFM),
    Event(datetime(2019, 1, 1, 7, 45), datetime(2019, 1, 1, 11, 45), FLIGHT, qls.BFM),

    Event(datetime(2019, 1, 1, 11, 15), datetime(2019, 1, 1, 14, 15), FLIGHT, qls.BFM),
    Event(datetime(2019, 1, 1, 11, 15), datetime(2019, 1, 1, 14, 15), FLIGHT, qls.BFM),
    Event(datetime(2019, 1, 1, 11, 15), datetime(2019, 1, 1, 15, 30), FLIGHT, qls.CAS, False),
    Event(datetime(2019, 1, 1, 11, 15), datetime(2019, 1, 1, 15, 30), FLIGHT, qls.FACA),
    Event(datetime(2019, 1, 1, 11, 15), datetime(2019, 1, 1, 15, 30), FLIGHT, qls.FACA, False),
    Event(datetime(2019, 1, 1, 11, 15), datetime(2019, 1, 1, 15, 30), FLIGHT, qls.CAS, False),
    Event(datetime(2019, 1, 1, 11, 15), datetime(2019, 1, 1, 15, 45), FLIGHT, qls.CAS, False),

    Event(datetime(2019, 1, 1, 12, 0), datetime(2019, 1, 1, 16, 0), FLIGHT, qls.BFM),
    Event(datetime(2019, 1, 1, 13, 0), datetime(2019, 1, 1, 17, 30), FLIGHT, qls.TRANS),
    Event(datetime(2019, 1, 1, 13, 0), datetime(2019, 1, 1, 17, 30), FLIGHT, qls.TRANS, False),
    Event(datetime(2019, 1, 1, 13, 15), datetime(2019, 1, 1, 17, 30), FLIGHT, qls.CAS),
    Event(datetime(2019, 1, 1, 13, 15), datetime(2019, 1, 1, 17, 30), FLIGHT, qls.FACA),
    Event(datetime(2019, 1, 1, 13, 15), datetime(2019, 1, 1, 17, 30), FLIGHT, qls.FACA, False),
    Event(datetime(2019, 1, 1, 13, 15), datetime(2019, 1, 1, 17, 30), FLIGHT, qls.CAS),

    Event(datetime(2019, 1, 1, 13, 45), datetime(2019, 1, 1, 17, 45), FLIGHT, qls.TRANS),
    Event(datetime(2019, 1, 1, 15, 15), datetime(2019, 1, 1, 19, 45), FLIGHT, qls.TRANS),
    Event(datetime(2019, 1, 1, 15, 15), datetime(2019, 1, 1, 19, 45), FLIGHT, qls.TRANS),
    Event(datetime(2019, 1, 1, 15, 15), datetime(2019, 1, 1, 19, 45), FLIGHT, qls.TRANS),
    Event(datetime(2019, 1, 1, 15, 15), datetime(2019, 1, 1, 19, 45), FLIGHT, qls.TRANS),
    Event(datetime(2019, 1, 1, 15, 15), datetime(2019, 1, 1, 19, 45), FLIGHT, qls.TRANS),

    Event(datetime(2019, 1, 1, 7, 0), datetime(2019, 1, 1, 12, 0), FLIGHT, qls.WEEN),
    Event(datetime(2019, 1, 1, 7, 0), datetime(2019, 1, 1, 12, 0), FLIGHT, qls.FACA, False),
    Event(datetime(2019, 1, 1, 13, 0), datetime(2019, 1, 1, 16, 0), FLIGHT, qls.WEEN),
    Event(datetime(2019, 1, 1, 13, 0), datetime(2019, 1, 1, 16, 0), FLIGHT, qls.FACA, False),

    # sims:
    Event(datetime(2019, 1, 1, 7, 0), datetime(2019, 1, 1, 10, 0), SIM, qls.TRANS, False),
    Event(datetime(2019, 1, 1, 7, 0), datetime(2019, 1, 1, 10, 30), SIM, qls.TRANS, False),
    Event(datetime(2019, 1, 1, 7, 30), datetime(2019, 1, 1, 11, 0), SIM, qls.STK, False),
    Event(datetime(2019, 1, 1, 9, 0), datetime(2019, 1, 1, 12, 45), SIM, qls.FACA),
    Event(datetime(2019, 1, 1, 9, 0), datetime(2019, 1, 1, 12, 45), SIM, qls.FACA, False),
    Event(datetime(2019, 1, 1, 9, 0), datetime(2019, 1, 1, 12, 45), SIM, qls.CAS),
    Event(datetime(2019, 1, 1, 11, 15), datetime(2019, 1, 1, 16, 15), SIM, qls.FACA),
    Event(datetime(2019, 1, 1, 12, 0), datetime(2019, 1, 1, 14, 30), SIM, qls.INST),
    Event(datetime(2019, 1, 1, 13, 15), datetime(2019, 1, 1, 15, 45), SIM, qls.FACA),
    Event(datetime(2019, 1, 1, 13, 15), datetime(2019, 1, 1, 15, 45), SIM, qls.FACA, False),
    Event(datetime(2019, 1, 1, 13, 15), datetime(2019, 1, 1, 15, 45), SIM, qls.CAS),
    Event(datetime(2019, 1, 1, 14, 0), datetime(2019, 1, 1, 15, 30), SIM, qls.TRANS),

    # classes:
    Event(datetime(2019, 1, 1, 9, 45), datetime(2019, 1, 1, 11, 15), CLS, qls.CAS, False),
    Event(datetime(2019, 1, 1, 11, 0), datetime(2019, 1, 1, 13, 0), CLS, qls.STK, False),
    Event(datetime(2019, 1, 1, 16, 0), datetime(2019, 1, 1, 17, 15), CLS, qls.BFM, False),
]

events = {event.id: event for event in _event_list}

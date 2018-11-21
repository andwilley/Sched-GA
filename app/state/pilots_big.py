from app.models.pilot import Pilot
from app.constants.quals import *

_pilot_list = [
    # Pilots
    Pilot("Foz", [TRANS, STK, FWT1, BFM, FCF]),
    Pilot("Kin", [TRANS, STK, CAS, FWT1, FCF]),
    Pilot("Metro", [TRANS, STK, CAS, NS, IFR, FWT1, FWT2, BFM, FCF, NTPS, INST, WEEN]),
    Pilot("MAWTS", [TRANS, STK, CAS, IFR, FWT1, FWT2, BFM, FCF, NTPS, INST]),
    Pilot("Flash", [TRANS, STK, CAS, FACA, FWT1, FCF, ODO], last_odo=14),
    # 5
    Pilot("Eeyore", [TRANS, STK, CAS, NS, IFR, FWT1, FWT2, BFM, FCF, NTPS, INST, ODO], last_odo=24),
    Pilot("Maj", [TRANS, STK, CAS, FWT1, FWT2, BFM, FCF, ODO], last_odo=1),
    Pilot("AARP", [TRANS, STK, FWT1, NTPS, INST, ODO], last_odo=1),
    Pilot("Junk", [TRANS, STK, FACA, CAS, IFR, FWT1, FWT2, FCF]),
    Pilot("Tummy", [TRANS, STK, LAT, CAS, IFR, FWT1, FCF, ODO, WEEN], last_odo=1),
    # 10
    Pilot("BF", [TRANS, STK, FWT1, CQ, WEEN]),
    Pilot("EITHA", [TRANS, STK, FWT1, NTPS, INST, ODO], last_odo=1),
    Pilot("Broke", [TRANS, ODO], last_odo=0),
    Pilot("Lumpy", [TRANS, STK, CAS, FWT1, FCF, NTPS, INST, ODO], last_odo=0),
    Pilot("Stallion", [TRANS, STK, LAT, CAS, ODO], last_odo=0),
    # 15
    Pilot("Squirrel", [TRANS, STK, CAS, IFR, FWT1, FCF, NTPS, INST, ODO, WEEN], last_odo=34),
    Pilot("Mongo", [TRANS, STK, FACA, CAS, FWT1, FWT2, BFM, FCF, ODO, WEEN], last_odo=0),
    Pilot("Busey", [TRANS, STK, CAS, FWT1, FCF, NTPS, INST, ODO, OCF, CQ, WEEN], last_odo=12),
    Pilot("NAGAA", [TRANS, STK, LAT, FACA, CAS, FWT1, FCF]),
    Pilot("Drub", [TRANS, STK, CAS, FWT1, FCF, NTPS, INST, ODO], last_odo=8),
    # 20
    Pilot("M&M", [TRANS, STK, CAS, FWT1, FWT2, BFM, FCF, NTPS, INST, ODO, WEEN], last_odo=3),
    Pilot("Mond", [TRANS, STK, CAS, NS, FWT1, ODO], last_odo=3),
    Pilot("Fonix", [TRANS, STK, FWT1, FCF, ODO], last_odo=15),
    Pilot("Barbie", [TRANS, STK, FACA, CAS, FWT1, BFM, FCF, NTPS, INST, ODO], last_odo=18),
    Pilot("Lefty", [TRANS, STK, CAS, FWT1, NTPS, INST, ODO, WEEN], last_odo=23),
    # 25
    Pilot("Shack", [TRANS, STK, LAT, CAS, NS, FWT1, FWT2, BFM, FCF, ODO], last_odo=11),
    Pilot("2Face", [TRANS, STK, CAS, FWT1, ODO], last_odo=5),
    Pilot("Landfill", [TRANS, STK, CAS, FWT1, CQ, ODO, WEEN], last_odo=5),
    Pilot("Coots", [TRANS, STK, CAS, IFR, FWT1, FCF, ODO, WEEN], last_odo=26),
    Pilot("Face", [TRANS, STK, CAS, FWT1, FWT2, BFM]),
    # 30
    Pilot("BS", [TRANS, STK, LAT, CAS, FWT1, FWT2, BFM, FCF, ODO], last_odo=21),
    Pilot("Repo", [TRANS, STK, CAS, FWT1, FWT2, FCF, ODO, WEEN], last_odo=4),
    Pilot("Foam", [TRANS, STK, LAT, CAS, FWT1, FWT2, BFM, FCF]),

    # WSOs
    Pilot("Cougar", [TRANS, STK, FACA, CAS, FWT1, ODO], plt=False, last_odo=17),
    Pilot("Milio", [TRANS, STK, FACA, CAS, FWT1, FWT2, BFM, ODO], plt=False, last_odo=16),
    # 35
    Pilot("Barney", [TRANS, STK, FACA, CAS, FWT1, FWT2, ODO], plt=False, last_odo=13),
    Pilot("Turtle", [TRANS, STK, FACA, CAS, FWT1, FWT2, BFM], plt=False),
    Pilot("Steam", [TRANS, STK, FACA, CAS, FWT1], plt=False),
]

pilots = {pilot.id: pilot for pilot in _pilot_list}

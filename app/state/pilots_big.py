from app.models.pilot import Pilot
from app.constants.quals import *

_pilot_list = [
    # Pilots
    Pilot("Foz", [TRANS, STK, FWT1, BFM, FCF]),
    Pilot("Kin", [TRANS, STK, CAS, FWT1, FCF]),
    Pilot("Metro", [TRANS, STK, CAS, NS, IFR, FWT1, FWT2, BFM, FCF, NTPS, INST, WEEN]),
    Pilot("MAWTS", [TRANS, STK, CAS, IFR, FWT1, FWT2, BFM, FCF, NTPS, INST]),
    Pilot("Flash", [TRANS, STK, CAS, FACA, FWT1, FCF, ODO]),
    # 5
    Pilot("Eeyore", [TRANS, STK, CAS, NS, IFR, FWT1, FWT2, BFM, FCF, NTPS, INST, ODO]),
    Pilot("Maj", [TRANS, STK, CAS, FWT1, FWT2, BFM, FCF, ODO]),
    Pilot("AARP", [TRANS, STK, FWT1, NTPS, INST, ODO]),
    Pilot("Junk", [TRANS, STK, FACA, CAS, IFR, FWT1, FWT2, FCF]),
    Pilot("Tummy", [TRANS, STK, LAT, CAS, IFR, FWT1, FCF, ODO, WEEN]),
    # 10
    Pilot("BF", [TRANS, STK, FWT1, CQ, WEEN]),
    Pilot("EITHA", [TRANS, STK, FWT1, NTPS, INST, ODO]),
    Pilot("Broke", [TRANS, ODO]),
    Pilot("Lumpy", [TRANS, STK, CAS, FWT1, FCF, NTPS, INST, ODO]),
    Pilot("Stallion", [TRANS, STK, LAT, CAS, ODO]),
    # 15
    Pilot("Squirrel", [TRANS, STK, CAS, IFR, FWT1, FCF, NTPS, INST, ODO, WEEN]),
    Pilot("Mongo", [TRANS, STK, FACA, CAS, FWT1, FWT2, BFM, FCF, ODO, WEEN]),
    Pilot("Busey", [TRANS, STK, CAS, FWT1, FCF, NTPS, INST, ODO, OCF, CQ, WEEN]),
    Pilot("NAGAA", [TRANS, STK, LAT, FACA, CAS, FWT1, FCF]),
    Pilot("Drub", [TRANS, STK, CAS, FWT1, FCF, NTPS, INST, ODO]),
    # 20
    Pilot("M&M", [TRANS, STK, CAS, FWT1, FWT2, BFM, FCF, NTPS, INST, ODO, WEEN]),
    Pilot("Mond", [TRANS, STK, CAS, NS, FWT1, ODO]),
    Pilot("Fonix", [TRANS, STK, FWT1, FCF, ODO]),
    Pilot("Barbie", [TRANS, STK, FACA, CAS, FWT1, BFM, FCF, NTPS, INST, ODO]),
    Pilot("Lefty", [TRANS, STK, CAS, FWT1, NTPS, INST, ODO, WEEN]),
    # 25
    Pilot("Shack", [TRANS, STK, LAT, CAS, NS, FWT1, FWT2, BFM, FCF, ODO]),
    Pilot("2Face", [TRANS, STK, CAS, FWT1, ODO]),
    Pilot("Landfill", [TRANS, STK, CAS, FWT1, CQ, ODO, WEEN]),
    Pilot("Coots", [TRANS, STK, CAS, IFR, FWT1, FCF, ODO, WEEN]),
    Pilot("Face", [TRANS, STK, CAS, FWT1, FWT2, BFM]),
    # 30
    Pilot("BS", [TRANS, STK, LAT, CAS, FWT1, FWT2, BFM, FCF, ODO]),
    Pilot("Repo", [TRANS, STK, CAS, FWT1, FWT2, FCF, ODO, WEEN]),
    Pilot("Foam", [TRANS, STK, LAT, CAS, FWT1, FWT2, BFM, FCF]),

    # WSOs
    Pilot("Cougar", [TRANS, STK, FWT1], plt=False),
    Pilot("Milio", [TRANS, STK, FACA, CAS, FWT1, FWT2, BFM, ODO], plt=False),
    # 35
    Pilot("Barney", [TRANS, STK, FACA, CAS, FWT1, FWT2, ODO], plt=False),
    Pilot("Turtle", [TRANS, STK, FACA, CAS, FWT1, FWT2, BFM], plt=False),
    Pilot("Steam", [TRANS, STK, FACA, CAS, FWT1], plt=False),
]

pilots = {pilot.id: pilot for pilot in _pilot_list}

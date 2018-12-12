from app.models.pilot import Pilot
from app.constants.quals import *

_pilot_list = [
    # Pilots (38)
    Pilot("plt0", [TRANS, STK, FWT1, BFM, FCF]),
    Pilot("plt1", [TRANS, STK, CAS, FWT1, FCF]),
    Pilot("plt2", [TRANS, STK, CAS, NS, IFR, FWT1, FWT2, BFM, FCF, NTPS, INST, WEEN]),
    Pilot("plt3", [TRANS, STK, CAS, IFR, FWT1, FWT2, BFM, FCF, NTPS, INST]),
    Pilot("plt4", [TRANS, STK, CAS, FACA, FWT1, FCF, ODO], last_odo=14),
    # 5
    Pilot("plt5", [TRANS, STK, CAS, NS, IFR, FWT1, FWT2, BFM, FCF, NTPS, INST, ODO], last_odo=24),
    Pilot("plt6", [TRANS, STK, CAS, FWT1, FWT2, BFM, FCF, ODO], last_odo=1),
    Pilot("plt7", [TRANS, STK, FWT1, NTPS, INST, ODO], last_odo=1),
    Pilot("plt8", [TRANS, STK, FACA, CAS, IFR, FWT1, FWT2, FCF]),
    Pilot("plt9", [TRANS, STK, LAT, CAS, IFR, FWT1, FCF, ODO, WEEN], last_odo=1),
    # 10
    Pilot("plt10", [TRANS, STK, FWT1, CQ, WEEN]),
    Pilot("plt11", [TRANS, STK, FWT1, NTPS, INST, ODO], last_odo=1),
    Pilot("plt12", [TRANS, ODO], last_odo=0),
    Pilot("plt13", [TRANS, STK, CAS, FWT1, FCF, NTPS, INST, ODO], last_odo=0),
    Pilot("plt14", [TRANS, STK, LAT, CAS, ODO], last_odo=0),
    # 15
    Pilot("plt15", [TRANS, STK, CAS, IFR, FWT1, FCF, NTPS, INST, ODO, WEEN], last_odo=34),
    Pilot("plt16", [TRANS, STK, FACA, CAS, FWT1, FWT2, BFM, FCF, ODO, WEEN], last_odo=0),
    Pilot("plt17", [TRANS, STK, CAS, FWT1, FCF, NTPS, INST, ODO, OCF, CQ, WEEN], last_odo=12),
    Pilot("plt18", [TRANS, STK, LAT, FACA, CAS, FWT1, FCF]),
    Pilot("plt19", [TRANS, STK, CAS, FWT1, FCF, NTPS, INST, ODO], last_odo=8),
    # 20
    Pilot("plt20", [TRANS, STK, CAS, FWT1, FWT2, BFM, FCF, NTPS, INST, ODO, WEEN], last_odo=3),
    Pilot("plt21", [TRANS, STK, CAS, NS, FWT1, ODO], last_odo=3),
    Pilot("plt22", [TRANS, STK, FWT1, FCF, ODO], last_odo=15),
    Pilot("plt23", [TRANS, STK, FACA, CAS, FWT1, BFM, FCF, NTPS, INST, ODO], last_odo=18),
    Pilot("plt24", [TRANS, STK, CAS, FWT1, NTPS, INST, ODO, WEEN], last_odo=23),
    # 25
    Pilot("plt25", [TRANS, STK, LAT, CAS, NS, FWT1, FWT2, BFM, FCF, ODO], last_odo=11),
    Pilot("plt26", [TRANS, STK, CAS, FWT1, ODO], last_odo=5),
    Pilot("plt27", [TRANS, STK, CAS, FWT1, CQ, ODO, WEEN], last_odo=5),
    Pilot("plt28", [TRANS, STK, CAS, IFR, FWT1, FCF, ODO, WEEN], last_odo=26),
    Pilot("plt29", [TRANS, STK, CAS, FWT1, FWT2, BFM]),
    # 30
    Pilot("plt30", [TRANS, STK, LAT, CAS, FWT1, FWT2, BFM, FCF, ODO], last_odo=21),
    Pilot("plt31", [TRANS, STK, CAS, FWT1, FWT2, FCF, ODO, WEEN], last_odo=4),
    Pilot("plt32", [TRANS, STK, LAT, CAS, FWT1, FWT2, BFM, FCF]),

    # WSOs
    Pilot("wso0", [TRANS, STK, FACA, CAS, FWT1, ODO], plt=False, last_odo=17),
    Pilot("wso1", [TRANS, STK, FACA, CAS, FWT1, FWT2, BFM, ODO], plt=False, last_odo=16),
    # 35
    Pilot("wso2", [TRANS, STK, FACA, CAS, FWT1, FWT2, ODO], plt=False, last_odo=13),
    Pilot("wso3", [TRANS, STK, FACA, CAS, FWT1, FWT2, BFM], plt=False),
    Pilot("wso4", [TRANS, STK, FACA, CAS, FWT1], plt=False),
]

pilots = {pilot.id: pilot for pilot in _pilot_list}

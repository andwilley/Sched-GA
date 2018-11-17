from app.models.pilot import Pilot
from app.constants.quals import TRANS, STK, A2A, CQ

pilot1 = Pilot("Steam", [TRANS, STK, A2A])
pilot2 = Pilot("Virgil", [TRANS, A2A])
pilot3 = Pilot("Dump", [TRANS, STK, A2A])
pilot4 = Pilot("Beef", [TRANS])
pilot5 = Pilot("Space", [TRANS, STK])
pilot6 = Pilot("Jambles", [TRANS, STK])
pilot7 = Pilot("Cox", [TRANS, STK, CQ])
pilot8 = Pilot("Tummy", [TRANS, STK, CQ])

pilots = {
    pilot1.id: pilot1,
    pilot2.id: pilot2,
    pilot3.id: pilot3,
    pilot4.id: pilot4,
    pilot5.id: pilot5,
    pilot6.id: pilot6,
    pilot7.id: pilot7,
    pilot8.id: pilot8,
}

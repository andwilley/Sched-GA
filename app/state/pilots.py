from app.models.pilot import Pilot
import app.constants.quals as quls

pilot1 = Pilot("Steam", [quls.TRANS, quls.STK, quls.FWT1])
pilot2 = Pilot("Virgil", [quls.TRANS, quls.FWT1])
pilot3 = Pilot("Dump", [quls.TRANS, quls.STK, quls.FWT1])
pilot4 = Pilot("Beef", [quls.TRANS], plt=False)
pilot5 = Pilot("Space", [quls.TRANS, quls.STK])
pilot6 = Pilot("Jambles", [quls.TRANS, quls.STK])
pilot7 = Pilot("Cox", [quls.TRANS, quls.STK, quls.CQ])
pilot8 = Pilot("Tummy", [quls.TRANS, quls.STK, quls.CQ])

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

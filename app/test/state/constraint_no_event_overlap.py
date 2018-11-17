import uuid
from typing import Dict
from datetime import datetime
from app.models.event import Event
from app.models.pilot import Pilot
from app.models.event_gene import EventGene
from app.constants.quals import TRANS

"""
Event Overlap test state (1x)
"""

#                 |-----------b/l-----------|
#          |---a---|
#                                         |-----b-----|
#                       |-----c----|
#                                                          |--d--|
#                                                                |--e---|
# |-f-|
# |-g-|
# total of 3 overlaps

# baseline event
event11 = Event(datetime(2019, 1, 1, 10, 0), datetime(2019, 1, 1, 11, 0), "flight", TRANS)
# a - overlap start
event12 = Event(datetime(2019, 1, 1, 9, 30), datetime(2019, 1, 1, 10, 1), "flight", TRANS)
# b - overlap end
event13 = Event(datetime(2019, 1, 1, 10, 59), datetime(2019, 1, 1, 11, 30), "flight", TRANS)
# c - total overlap
event14 = Event(datetime(2019, 1, 1, 10, 20), datetime(2019, 1, 1, 10, 40), "flight", TRANS)
# d - does not conflict
event15 = Event(datetime(2019, 1, 1, 13, 0), datetime(2019, 1, 1, 14, 0), "flight", TRANS)
# e - does not conflict (end and start same)
event16 = Event(datetime(2019, 1, 1, 14, 0), datetime(2019, 1, 1, 15, 0), "flight", TRANS)
# f - full overlap with g
event17 = Event(datetime(2019, 1, 1, 8, 0), datetime(2019, 1, 1, 9, 0), "flight", TRANS)
# g - full overlap with f
event18 = Event(datetime(2019, 1, 1, 8, 0), datetime(2019, 1, 1, 9, 0), "flight", TRANS)

events_overlap: Dict[uuid.UUID, Event] = {
    event11.id: event11,
    event12.id: event12,
    event13.id: event13,
    event14.id: event14,
    event15.id: event15,
    event16.id: event16,
    event17.id: event17,
    event18.id: event18,
}

# pilots
pilot11 = Pilot("Steam", [TRANS])
pilots_overlap = {pilot11.id: pilot11}

# make event genes
gene11 = EventGene(event11.id)
gene11.pilot_id = pilot11.id

gene12 = EventGene(event12.id)
gene12.pilot_id = pilot11.id

gene13 = EventGene(event13.id)
gene13.pilot_id = pilot11.id

gene14 = EventGene(event14.id)
gene14.pilot_id = pilot11.id

gene15 = EventGene(event15.id)
gene15.pilot_id = pilot11.id

gene16 = EventGene(event16.id)
gene16.pilot_id = pilot11.id

gene17 = EventGene(event17.id)
gene17.pilot_id = pilot11.id

gene18 = EventGene(event18.id)
gene18.pilot_id = pilot11.id

# make individual
indiv_overlap = [gene11, gene12, gene13, gene14, gene15, gene16, gene17, gene18]

# problematic test case:
eventa = Event(datetime(2019, 1, 1, 7, 0), datetime(2019, 1, 1, 9, 0), "flight", TRANS)
eventb = Event(datetime(2019, 1, 1, 7, 0), datetime(2019, 1, 1, 9, 0), "flight", TRANS)
eventc = Event(datetime(2019, 1, 1, 10, 0), datetime(2019, 1, 1, 11, 0), "flight", TRANS)
eventd = Event(datetime(2019, 1, 1, 10, 0), datetime(2019, 1, 1, 11, 0), "flight", TRANS)
evente = Event(datetime(2019, 1, 1, 15, 0), datetime(2019, 1, 1, 16, 0), "flight", TRANS)
eventf = Event(datetime(2019, 1, 1, 15, 0), datetime(2019, 1, 1, 16, 0), "flight", TRANS)
eventg = Event(datetime(2019, 1, 1, 18, 0), datetime(2019, 1, 1, 19, 0), "flight", TRANS)
eventh = Event(datetime(2019, 1, 1, 18, 0), datetime(2019, 1, 1, 19, 0), "flight", TRANS)
eventi = Event(datetime(2019, 1, 1, 21, 0), datetime(2019, 1, 1, 22, 0), "flight", TRANS)
eventj = Event(datetime(2019, 1, 1, 21, 0), datetime(2019, 1, 1, 22, 0), "flight", TRANS)

spec_events: Dict[uuid.UUID, Event] = {
    eventa.id: eventa,
    eventb.id: eventb,
    eventc.id: eventc,
    eventd.id: eventd,
    evente.id: evente,
    eventf.id: eventf,
    eventg.id: eventg,
    eventh.id: eventh,
    eventi.id: eventi,
    eventj.id: eventj,
}

pilota = Pilot("Steam", [TRANS])
pilotb = Pilot("Virgil", [TRANS])
pilotc = Pilot("Dump", [TRANS])
pilotd = Pilot("Beef", [TRANS])
pilote = Pilot("Space", [TRANS])
pilotf = Pilot("Jambles", [TRANS])
pilotg = Pilot("Cox", [TRANS])
piloth = Pilot("Tummy", [TRANS])

spec_pilots = {
    pilota.id: pilota,
    pilotb.id: pilotb,
    pilotc.id: pilotc,
    pilotd.id: pilotd,
    pilote.id: pilote,
    pilotf.id: pilotf,
    pilotg.id: pilotg,
    piloth.id: piloth,
}

genea = EventGene(eventa.id)
genea.pilot_id = pilotg.id

geneb = EventGene(eventb.id)
geneb.pilot_id = pilotg.id

genec = EventGene(eventc.id)
genec.pilot_id = piloth.id

gened = EventGene(eventd.id)
gened.pilot_id = pilotg.id

genee = EventGene(evente.id)
genee.pilot_id = piloth.id

genef = EventGene(eventf.id)
genef.pilot_id = pilotf.id

geneg = EventGene(eventg.id)
geneg.pilot_id = pilote.id

geneh = EventGene(eventh.id)
geneh.pilot_id = pilote.id

genei = EventGene(eventi.id)
genei.pilot_id = piloth.id

genej = EventGene(eventj.id)
genej.pilot_id = pilotc.id

spec_indiv = [genea, geneb, genec, gened, genee, genef, geneg, geneh, genei, genej]

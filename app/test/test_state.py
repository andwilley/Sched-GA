import uuid
from typing import Dict
from datetime import datetime
from app.models.event import Event
from app.models.pilot import Pilot
from app.models.event_gene import EventGene

"""
Crew Day test state (x)
"""

# violates day crew day by 1 hour
event1 = Event(datetime(2019, 1, 1, 6, 0), datetime(2019, 1, 1, 7, 0), "flight")
event2 = Event(datetime(2019, 1, 1, 18, 0), datetime(2019, 1, 1, 19, 0), "flight")

# violates night crew day by 2 hours
event3 = Event(datetime(2019, 1, 1, 10, 0), datetime(2019, 1, 1, 11, 0), "flight")
event4 = Event(datetime(2019, 1, 1, 21, 0), datetime(2019, 1, 1, 22, 0), "flight")

# does not violate crew day
event5 = Event(datetime(2019, 1, 1, 10, 0), datetime(2019, 1, 1, 11, 0), "flight")
event6 = Event(datetime(2019, 1, 1, 12, 0), datetime(2019, 1, 1, 13, 0), "flight")

# total violation 180 minutes ( 3 hours )

events: Dict[uuid.UUID, Event] = {
    event1.id: event1,
    event2.id: event2,
    event3.id: event3,
    event4.id: event4,
    event5.id: event5,
}

# 3 pilots
pilot1 = Pilot()
pilot2 = Pilot()
pilot3 = Pilot()

cd_pilots = {
    pilot1.id: pilot1,
    pilot2.id: pilot2,
    pilot3.id: pilot3,
}

# make event genes
gene1 = EventGene(event1.id)
gene1.pilot_id = pilot1.id

gene2 = EventGene(event2.id)
gene2.pilot_id = pilot1.id

gene3 = EventGene(event3.id)
gene3.pilot_id = pilot2.id

gene4 = EventGene(event4.id)
gene4.pilot_id = pilot2.id

gene5 = EventGene(event5.id)
gene5.pilot_id = pilot3.id

# make individual
indiv_crewday = [gene1, gene2, gene3, gene4, gene5]

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
event11 = Event(datetime(2019, 1, 1, 10, 0), datetime(2019, 1, 1, 11, 0), "flight")
# a - overlap start
event12 = Event(datetime(2019, 1, 1, 9, 30), datetime(2019, 1, 1, 10, 1), "flight")
# b - overlap end
event13 = Event(datetime(2019, 1, 1, 10, 59), datetime(2019, 1, 1, 11, 30), "flight")
# c - total overlap
event14 = Event(datetime(2019, 1, 1, 10, 20), datetime(2019, 1, 1, 10, 40), "flight")
# d - does not conflict
event15 = Event(datetime(2019, 1, 1, 13, 0), datetime(2019, 1, 1, 14, 0), "flight")
# e - does not conflict (end and start same)
event16 = Event(datetime(2019, 1, 1, 14, 0), datetime(2019, 1, 1, 15, 0), "flight")
# f - full overlap with g
event17 = Event(datetime(2019, 1, 1, 8, 0), datetime(2019, 1, 1, 9, 0), "flight")
# g - full overlap with f
event18 = Event(datetime(2019, 1, 1, 8, 0), datetime(2019, 1, 1, 9, 0), "flight")

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
pilot11 = Pilot()
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
eventa = Event(datetime(2019, 1, 1, 7, 0), datetime(2019, 1, 1, 9, 0), "flight")
eventb = Event(datetime(2019, 1, 1, 7, 0), datetime(2019, 1, 1, 9, 0), "flight")
eventc = Event(datetime(2019, 1, 1, 10, 0), datetime(2019, 1, 1, 11, 0), "flight")
eventd = Event(datetime(2019, 1, 1, 10, 0), datetime(2019, 1, 1, 11, 0), "flight")
evente = Event(datetime(2019, 1, 1, 15, 0), datetime(2019, 1, 1, 16, 0), "flight")
eventf = Event(datetime(2019, 1, 1, 15, 0), datetime(2019, 1, 1, 16, 0), "flight")
eventg = Event(datetime(2019, 1, 1, 18, 0), datetime(2019, 1, 1, 19, 0), "flight")
eventh = Event(datetime(2019, 1, 1, 18, 0), datetime(2019, 1, 1, 19, 0), "flight")
eventi = Event(datetime(2019, 1, 1, 21, 0), datetime(2019, 1, 1, 22, 0), "flight")
eventj = Event(datetime(2019, 1, 1, 21, 0), datetime(2019, 1, 1, 22, 0), "flight")

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

pilota = Pilot("Steam")
pilotb = Pilot("Virgil")
pilotc = Pilot("Dump")
pilotd = Pilot("Beef")
pilote = Pilot("Space")
pilotf = Pilot("Jambles")
pilotg = Pilot("Cox")
piloth = Pilot("Tummy")

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


"""
operators test state
"""

# event ids
uuid1 = uuid.UUID('00000000-0000-0000-0000-000000000001')
uuid2 = uuid.UUID('00000000-0000-0000-0000-000000000002')
uuid3 = uuid.UUID('00000000-0000-0000-0000-000000000003')

# events
event30 = Event(datetime(2019, 1, 1, 7, 0), datetime(2019, 1, 1, 8, 0), "flight")
event30.id = uuid1
event31 = Event(datetime(2019, 1, 1, 7, 0), datetime(2019, 1, 1, 8, 0), "flight")
event31.id = uuid2
event32 = Event(datetime(2019, 1, 1, 9, 0), datetime(2019, 1, 1, 10, 0), "flight")
event32.id = uuid3

op_events = {
    event30.id: event30,
    event31.id: event31,
    event32.id: event32,
}

# pilots
pilot30 = Pilot("Steamboat")
pilot31 = Pilot("Dump")
pilot32 = Pilot("Tummy")
pilot33 = Pilot("Virgil")
pilot34 = Pilot("Topper")
pilot35 = Pilot("Spacecamp")
pilot36 = Pilot("Jambles")
pilot37 = Pilot("Beef")
pilot38 = Pilot("Donk")

op_pilots = {
    pilot30.id: pilot30,
    pilot31.id: pilot31,
    pilot32.id: pilot32,
    pilot33.id: pilot33,
    pilot34.id: pilot34,
    pilot35.id: pilot35,
    pilot36.id: pilot36,
    pilot37.id: pilot37,
    pilot38.id: pilot38,
}

schedule = [EventGene(uuid1), EventGene(uuid2), EventGene(uuid3)]

sched_alleles = {
    uuid1: [pilot30.id, pilot31.id, pilot32.id],
    uuid2: [pilot33.id, pilot34.id, pilot35.id],
    uuid3: [pilot36.id, pilot37.id, pilot38.id],
}

"""
Population Test State (2x)
"""

event20 = Event(datetime(2019, 1, 1, 7, 0), datetime(2019, 1, 1, 8, 0), "flight")
event21 = Event(datetime(2019, 1, 1, 7, 0), datetime(2019, 1, 1, 8, 0), "flight")
event22 = Event(datetime(2019, 1, 1, 9, 0), datetime(2019, 1, 1, 10, 0), "flight")
event23 = Event(datetime(2019, 1, 1, 9, 0), datetime(2019, 1, 1, 10, 0), "flight")
event24 = Event(datetime(2019, 1, 1, 13, 0), datetime(2019, 1, 1, 14, 0), "flight")
event25 = Event(datetime(2019, 1, 1, 13, 0), datetime(2019, 1, 1, 14, 0), "flight")
event26 = Event(datetime(2019, 1, 1, 14, 0), datetime(2019, 1, 1, 15, 0), "flight")
event27 = Event(datetime(2019, 1, 1, 14, 0), datetime(2019, 1, 1, 15, 0), "flight")
event28 = Event(datetime(2019, 1, 1, 22, 0), datetime(2019, 1, 1, 23, 0), "flight")
event29 = Event(datetime(2019, 1, 1, 22, 0), datetime(2019, 1, 1, 23, 0), "flight")

pilot20 = Pilot("Steamboat")
pilot21 = Pilot("Dump")
pilot22 = Pilot("Tummy")
pilot23 = Pilot("Virgil")
pilot24 = Pilot("Topper")
pilot25 = Pilot("Spacecamp")
pilot26 = Pilot("Jambles")
pilot27 = Pilot("Beef")

pop_pilots = {
    pilot20.id: pilot20,
    pilot21.id: pilot21,
    pilot22.id: pilot22,
    pilot23.id: pilot23,
    pilot24.id: pilot24,
    pilot25.id: pilot25,
    pilot26.id: pilot26,
    pilot27.id: pilot27,
}

pop_events = {
    event20.id: event20,
    event21.id: event21,
    event22.id: event22,
    event23.id: event23,
    event24.id: event24,
    event25.id: event25,
    event26.id: event26,
    event27.id: event27,
    event28.id: event28,
    event29.id: event29,
}

pop_sched = [
    EventGene(event20.id),
    EventGene(event21.id),
    EventGene(event22.id),
    EventGene(event23.id),
    EventGene(event24.id),
    EventGene(event25.id),
    EventGene(event26.id),
    EventGene(event27.id),
    EventGene(event28.id),
    EventGene(event29.id),
]

pop_sched_alleles = {
    event20.id: [pilot20.id, pilot21.id, pilot22.id, pilot23.id, pilot24.id, pilot25.id,
                 pilot26.id, pilot27.id],
    event21.id: [pilot20.id, pilot21.id, pilot22.id, pilot23.id, pilot24.id, pilot25.id,
                 pilot26.id, pilot27.id],
    event22.id: [pilot20.id, pilot21.id, pilot22.id, pilot23.id, pilot24.id, pilot25.id,
                 pilot26.id, pilot27.id],
    event23.id: [pilot20.id, pilot21.id, pilot22.id, pilot23.id, pilot24.id, pilot25.id,
                 pilot26.id, pilot27.id],
    event24.id: [pilot20.id, pilot21.id, pilot22.id, pilot23.id, pilot24.id, pilot25.id,
                 pilot26.id, pilot27.id],
    event25.id: [pilot20.id, pilot21.id, pilot22.id, pilot23.id, pilot24.id, pilot25.id,
                 pilot26.id, pilot27.id],
    event26.id: [pilot20.id, pilot21.id, pilot22.id, pilot23.id, pilot24.id, pilot25.id,
                 pilot26.id, pilot27.id],
    event27.id: [pilot20.id, pilot21.id, pilot22.id, pilot23.id, pilot24.id, pilot25.id,
                 pilot26.id, pilot27.id],
    event28.id: [pilot20.id, pilot21.id, pilot22.id, pilot23.id, pilot24.id, pilot25.id,
                 pilot26.id, pilot27.id],
    event29.id: [pilot20.id, pilot21.id, pilot22.id, pilot23.id, pilot24.id, pilot25.id,
                 pilot26.id, pilot27.id],
}

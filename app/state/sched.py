"""
Module globals are probably a bad idea, but I don't have time to implement proper state
management for this project, nor is there really a pressing need at this point, given
the way the appliction will be run.
"""
import uuid
from app.models.event_gene import EventGene

# event ids
uuid1 = uuid.UUID('00000000-0000-0000-0000-000000000001')
uuid2 = uuid.UUID('00000000-0000-0000-0000-000000000002')
uuid3 = uuid.UUID('00000000-0000-0000-0000-000000000003')

# pilot ids
uuid11 = uuid.UUID('00000000-0000-0000-0000-000000000011')
uuid12 = uuid.UUID('00000000-0000-0000-0000-000000000012')
uuid13 = uuid.UUID('00000000-0000-0000-0000-000000000013')
uuid14 = uuid.UUID('00000000-0000-0000-0000-000000000014')
uuid15 = uuid.UUID('00000000-0000-0000-0000-000000000015')
uuid16 = uuid.UUID('00000000-0000-0000-0000-000000000016')
uuid17 = uuid.UUID('00000000-0000-0000-0000-000000000017')
uuid18 = uuid.UUID('00000000-0000-0000-0000-000000000018')
uuid19 = uuid.UUID('00000000-0000-0000-0000-000000000019')


schedule = [EventGene(uuid1), EventGene(uuid2), EventGene(uuid3)]

sched_alleles = {
    uuid1: [uuid11, uuid12, uuid13],
    uuid2: [uuid14, uuid15, uuid16],
    uuid3: [uuid17, uuid18, uuid19],
}

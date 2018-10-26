"""
Module globals are probably a bad idea, but I don't have time to implement proper state
management for this project, nor is there really a pressing need at this point, given
the way the appliction will be run.
"""
from models.event_gene import EventGene

schedule = [EventGene('a'), EventGene('b'), EventGene('c')]

sched_alleles = {
    'a': ['a', 'b', 'h'],
    'b': ['c', 'd', 'i'],
    'c': ['e', 'f', 'g'],
}

import unittest
from app.models.event_gene import EventGene

class EventGeneCase(unittest.TestCase):

    def test_initialize(self):
        event_gene = EventGene('a')
        self.assertEqual(event_gene.event_id, 'a', "Event id should be set.")

    def test_setters(self):
        event_gene = EventGene('a')
        event_gene.pilot_id = 'abc'
        self.assertEqual(event_gene.pilot_id, 'abc', "Pilot id should be set.")

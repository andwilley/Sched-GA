import unittest
from uuid import UUID
from app.models.pilot import Pilot

class PilotsCase(unittest.TestCase):

    def test_initialize(self):
        pilot = Pilot()
        print(pilot.id)
        self.assertTrue(isinstance(pilot.id, UUID), "The id field should be a string.")

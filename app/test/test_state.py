import unittest
from app.models.state import State
import app.test.state.state_test as st

class StateCase(unittest.TestCase):

    def test_alleles(self):
        state = State(st.pilots1, st.events2, st.snivs)
        # make sure it added snivs
        for _, pilot in state.pilots.items():
            if pilot.callsign == "Steam" or pilot.callsign == "Tummy":
                self.assertEqual(len(pilot.snivs), 1, "Sniv should have been added.")
            else:
                self.assertFalse(pilot.snivs, "Should be no snivs.")

        # make sure pilot availability it right
        self.assertEqual(state.alleles[st.event1.id], [st.pilot3.id], "event1") # dump
        self.assertEqual(state.alleles[st.event2.id], [st.pilot1.id, st.pilot3.id]) # dump steam
        self.assertEqual(state.alleles[st.event3.id], [st.pilot2.id, st.pilot3.id]) # dump virgil
        self.assertEqual(state.alleles[st.event5.id], [st.pilot2.id, st.pilot3.id]) # virgil dump

    def test_alleles_fail(self):
        # make sure it throws when no one is available
        self.assertRaises(ValueError, State, st.pilots2, st.events1, st.snivs)

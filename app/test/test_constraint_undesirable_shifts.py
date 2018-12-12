import unittest
from app.test.state.constraint_undesirable_shifts import indiv1, pilots, events
from app.models.constraints.undesirable_shifts import UndesirableShifts
from app.models.state import State
from app.ga.parameters import UNDESIRABLE_SHIFT_WEIGHT as WEIGHT
from app.ga.parameters import ODO_MULTIPLIER

class ConstraintUndesirableShiftsCase(unittest.TestCase):
    def test_initialize(self):
        state = State(pilots, events, {})
        undesirable_constraint = UndesirableShifts(state)
        self.assertEqual(undesirable_constraint.get_final_fitness(), 0.0, "Fitness should be set.")

    def test_each_event_with_penalty(self):

        state = State(pilots, events, {})
        undesirable_constraint = UndesirableShifts(state)

        for gene in indiv1:
            undesirable_constraint.each_event(gene)

        # pilots have 0, 2 * ODO MULT, and 2 undesirable events in the test set
        avg = (0 + 2 * ODO_MULTIPLIER + 2) / 3
        total = abs(0 - avg) + abs(2 * ODO_MULTIPLIER - avg) + abs(2 - avg)
        self.assertEqual(undesirable_constraint.get_final_fitness(), total * WEIGHT,
                         "Fitness should be 12 events.")

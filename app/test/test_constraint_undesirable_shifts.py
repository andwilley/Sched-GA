import unittest
from app.test.state.constraint_undesirable_shifts import indiv1, pilots, events
from app.models.constraints.undesirable_shifts import UndesirableShifts
from app.models.state import State
from app.ga.parameters import UNDESIRABLE_SHIFT_WEIGHT as WEIGHT

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

        self.assertEqual(undesirable_constraint.get_final_fitness(), 2.0 * WEIGHT,
                         "Fitness should be 2 events.")

import unittest
from app.test.state.constraint_last_odo import indiv1, indiv2, pilots, events
from app.models.constraints.last_odo import LastODO
from app.models.state import State
from app.ga.parameters import LAST_ODO_WEIGHT

class ConstraintFairWorkHoursCase(unittest.TestCase):
    # change to test_state events in crew_day.py
    def test_initialize(self):
        state = State(pilots, events, {})
        odo_constraint = LastODO(state)
        self.assertEqual(odo_constraint.get_final_fitness(), 0.0, "Fitness should be set.")

    def test_each_event_wrong_odo(self):

        state = State(pilots, events, {})
        odo_constraint = LastODO(state)

        for gene in indiv1:
            odo_constraint.each_event(gene)

        self.assertEqual(odo_constraint.get_final_fitness(), 1 * LAST_ODO_WEIGHT,
                         "Fitness should be 2.5.")

    def test_each_event_right_odo(self):

        state = State(pilots, events, {})
        odo_constraint = LastODO(state)

        for gene in indiv2:
            odo_constraint.each_event(gene)

        self.assertEqual(odo_constraint.get_final_fitness(), 0 * LAST_ODO_WEIGHT,
                         "Fitness should be 0.")

import unittest
from app.test.state.constraint_fair_work_test import indiv1, indiv2, pilots, events
from app.models.constraints.fair_work_hours import FairWorkHours
from app.models.state import State
from app.ga.parameters import FAIR_HOURS_WEIGHT

class ConstraintFairWorkHoursCase(unittest.TestCase):
    # change to test_state events in crew_day.py
    def test_initialize(self):
        state = State(pilots, events, {})
        fair_hours_constraint = FairWorkHours(state)
        self.assertEqual(fair_hours_constraint.get_final_fitness(), 0.0, "Fitness should be set.")

    def test_each_event_with_penalty(self):

        state = State(pilots, events, {})
        fair_hours_constraint = FairWorkHours(state)

        for gene in indiv1:
            fair_hours_constraint.each_event(gene)

        self.assertEqual(fair_hours_constraint.get_final_fitness(), 60 * 4 * FAIR_HOURS_WEIGHT,
                         "Fitness should be 4 hours.")

    def test_each_event_no_penalty(self):

        state = State(pilots, events, {})
        fair_hours_constraint = FairWorkHours(state)

        for gene in indiv2:
            fair_hours_constraint.each_event(gene)

        self.assertEqual(fair_hours_constraint.get_final_fitness(), 0,
                         "Fitness should be 0 hours.")

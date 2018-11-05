import unittest
from app.test.test_state import indiv_overlap
from app.models.constraints.no_event_overlap import NoEventOverlap

class ConstraintNoEventOverlapCase(unittest.TestCase):
    # change to test_state events in crew_day.py
    def test_initialize(self):
        no_overlap_constraint = NoEventOverlap()
        self.assertEqual(no_overlap_constraint.get_final_fitness(), 0.0, "Fitness should be set.")

    def test_each_event(self):

        no_overlap_constraint = NoEventOverlap()

        for gene in indiv_overlap:
            no_overlap_constraint.each_event(gene)

        self.assertEqual(no_overlap_constraint.get_final_fitness(), 3,
                         "Fitness should be 3 overlaps.")

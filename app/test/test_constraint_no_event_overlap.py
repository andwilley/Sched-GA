import unittest
from app.ga.parameters import OVERLAP_WEIGHT
from app.test.test_state import indiv_overlap, pilots_overlap, events_overlap
from app.models.constraints.no_event_overlap import NoEventOverlap
from app.models.state import State

class ConstraintNoEventOverlapCase(unittest.TestCase):
    # change to test_state events in crew_day.py
    def test_initialize(self):
        state = State(pilots_overlap, events_overlap)
        no_overlap_constraint = NoEventOverlap(state)
        self.assertEqual(no_overlap_constraint.get_final_fitness(), 0.0, "Fitness should be set.")

    def test_each_event(self):

        state = State(pilots_overlap, events_overlap)
        no_overlap_constraint = NoEventOverlap(state)

        for gene in indiv_overlap:
            no_overlap_constraint.each_event(gene)

        self.assertEqual(no_overlap_constraint.get_final_fitness(), 22 * OVERLAP_WEIGHT,
                         "Fitness should be 3 overlaps.")

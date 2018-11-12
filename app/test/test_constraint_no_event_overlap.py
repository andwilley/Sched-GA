import unittest
from app.ga.parameters import OVERLAP_WEIGHT
from app.test.state.constraint_no_event_overlap import indiv_overlap, pilots_overlap, \
                                                       events_overlap, spec_events,\
                                                       spec_pilots, spec_indiv
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

        self.assertEqual(no_overlap_constraint.get_final_fitness(), 82 * OVERLAP_WEIGHT,
                         "Fitness should be 4 overlaps.")

    def test_specific_individual_fitness(self):
        state = State(spec_pilots, spec_events)
        no_overlap_constraint = NoEventOverlap(state)

        for gene in spec_indiv:
            no_overlap_constraint.each_event(gene)

        self.assertEqual(no_overlap_constraint.get_final_fitness(), 180 * OVERLAP_WEIGHT,
                         "Fitness should be 4 overlaps.")

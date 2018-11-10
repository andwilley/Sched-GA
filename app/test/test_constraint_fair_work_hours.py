import unittest
from app.test.state.constraint_fair_work_test import indiv_crewday, cd_pilots, events
from app.models.constraints.crew_day import CrewDay
from app.models.state import State

class ConstraintFairWorkHoursCase(unittest.TestCase):
    # change to test_state events in crew_day.py
    def test_initialize(self):
        state = State(cd_pilots, events)
        crew_day_constraint = CrewDay(state)
        self.assertEqual(crew_day_constraint.get_final_fitness(), 0.0, "Fitness should be set.")

    def test_each_event(self):

        state = State(cd_pilots, events)
        crew_day_constraint = CrewDay(state)

        for gene in indiv_crewday:
            crew_day_constraint.each_event(gene)

        self.assertEqual(crew_day_constraint.get_final_fitness(), 60 * 3,
                         "Fitness should be 3 hours.")

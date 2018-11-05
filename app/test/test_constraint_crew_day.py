import unittest
from app.test.test_state import indiv_crewday
from app.models.constraints.crew_day import CrewDay

class ConstraintCrewDayCase(unittest.TestCase):
    # change to test_state events in crew_day.py
    def test_initialize(self):
        crew_day_constraint = CrewDay()
        self.assertEqual(crew_day_constraint.get_final_fitness(), 0.0, "Fitness should be set.")

    def test_each_event(self):

        crew_day_constraint = CrewDay()

        for gene in indiv_crewday:
            crew_day_constraint.each_event(gene)

        self.assertEqual(crew_day_constraint.get_final_fitness(), 60 * 3,
                         "Fitness should be 3 hours.")

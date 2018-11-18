"""
The GA parameters
"""

# General ga params
MAX_GEN = 200
POP_SIZE = 400

# Operator params
ELITE_RATIO = 0.2
DIVERSE_ELITE = True
X_OVER_PTS = 1
MUT_PROB = 0.01

# fitness weights
CREWDAY_WEIGHT = 5
OVERLAP_WEIGHT = 10
FAIR_HOURS_WEIGHT = 2
UNDESIRABLE_SHIFT_WEIGHT = 25

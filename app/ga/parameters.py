"""
The GA parameters
"""

# General population params
MAX_GEN = 100
POP_SIZE = 100

# Operator params
ELITE_RATIO = 0.2
DIVERSE_ELITE = True
X_OVER_PTS = 1
MUT_PROB = 0.01

# fitness weights
CREWDAY_WEIGHT = 5
OVERLAP_WEIGHT = 7
FAIR_HOURS_WEIGHT = 2

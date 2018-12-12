"""
The GA parameters
"""

# General ga params
MAX_GEN = 150           # 150
POP_SIZE = 400          # 400

# Operator params
ELITE_RATIO = 0.2       # 0.2
DIVERSE_ELITE = True    # True
X_OVER_PTS = 3          # 3
MUT_PROB = 0.01         # 0.01

# fitness weights
CREWDAY_WEIGHT = 200            # 200
OVERLAP_WEIGHT = 100            # 100
FAIR_HOURS_WEIGHT = 1           # 1
UNDESIRABLE_SHIFT_WEIGHT = 200  # 200
LAST_ODO_WEIGHT = 1200          # 1200

# ODO specific event penalty
ODO_MULTIPLIER = 5

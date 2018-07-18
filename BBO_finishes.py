# A python program to calculate whether a 1st place
# tie is possible in the Boneyard Build-Off
from itertools import permutations
import numpy as np
from collections import Counter

#Number of teams
n_teams = 4

#variables
poss_ties = 0
scenarios = []

perms = list(permutations(range(1,n_teams+1)))

for race in perms:
    for garbage in perms:
        for cool in perms:
            score = np.array(race)+np.array(garbage)+np.array(cool)
            tied = [item for item, count in Counter(score).most_common(1) if count > 1]
            if tied:
                if tied[0] == score.max():
                    poss_ties += 1
                    scenarios.append([race,garbage,cool])

print(poss_ties, poss_ties/24**3)
# print(scenarios)
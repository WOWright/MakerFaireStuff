# A python program to calculate whether a 1st place
# tie is possible in the Boneyard Build-Off
import itertools as it
import numpy as np
from collections import Counter

#Number of teams
n_teams = 4

#Number of categories
n_cats = 3

#variables
poss_ties = 0
scenarios = []
finals = []

perms = it.permutations(range(1,n_teams+1))
outcomes = it.permutations(perms, n_cats)

for event in outcomes:
    finals.append(tuple(sum(x) for x in zip(*event)))
    tied = [item for item, count in Counter(finals[-1]).most_common(1) if count > 1]
    if tied:
        if tied[0] == max(finals[-1]):
            poss_ties += 1
            # scenarios.append(finals[-1])

print(poss_ties, poss_ties/24**3)
# print(finals)

poss_ties = 0
permutes = list(it.permutations(range(1,n_teams+1)))
for race in permutes:
    for garbage in permutes:
        for cool in permutes:
            score = np.array(race)+np.array(garbage)+np.array(cool)
            tied = [item for item, count in Counter(score).most_common(1) if count > 1]
            if tied:
                if tied[0] == score.max():
                    poss_ties += 1
                    # scenarios.append(score)

print(poss_ties, poss_ties/24**3)
# print(scenarios)
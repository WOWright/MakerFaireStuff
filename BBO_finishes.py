# A python program to calculate whether a 1st place
# tie is possible in the Boneyard Build-Off
from itertools import permutations, product
import numpy as np
from collections import Counter

# Number of competitions
n_competitions = 3

# Define points used in competition
points = [1,2,3,4]

# variables
poss_ties = 0
scenarios = []

# Tie test
def isFirstPlaceTied(score):
    score.sort()
    return score[-1] == score[-2] #test to see if the two largest are equal

# generate all possible outcomes of a competition
competitions = list(permutations(points))

# combine multiple competitions 
outcomes = list(product(competitions, repeat=n_competitions))

# sum up the competitions
final_scores = np.array(outcomes).sum(1).tolist()

# check for ties
isTied = [isFirstPlaceTied(score) for score in final_scores]

# count ties
numTied = isTied.count(True)

# calculate percentages
percentTied = numTied / len(final_scores)

# print result
print(percentTied)
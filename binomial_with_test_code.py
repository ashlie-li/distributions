#The binomial distribution describes the probability of obtaining k successes in n binomial experiments.
# The formula is: P(X=k) = nCk * p**k * (1-p)**(n-k). where:
#n: number of trials
#k: number of successes
#p: probability of success on a given trial.
#nCk: the number of ways to obtain k successes in n trials.

from numpy import random
random.binomial(n=0, p=0, size=None)


#test example: generate an array of 10 values that follow a binomial distribution with 5 trail and the pprobability of success is 0.25.
random.binomial(n=5, p=.25, size=10)

import unittest

class TestingBinomial(unittest.TestCase):
  def test_within_range(self):
    result = random.binomial(n=5, p=.25, size=10)
    print(result)
    length = len(result) == 10
    self.assertTrue(length)

#sample output:
#array([2, 1, 1, 0, 1, 0, 1, 2, 1, 3])
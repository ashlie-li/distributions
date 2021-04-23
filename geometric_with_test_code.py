#The geometric distribution represents the number of failures before you get a success in a series of Bernoulli trials.
#The discrete probability distribution function: f(x) = (1 − p)**(x − 1)*p
#p: the probability of success of an individual trial.
#K: the number of trials that must be run in order to achieve success.

from numpy import random
random.geometric(p=0.1, size=None)

#Draw ten values from the geometric distribution, with the probability of an individual success equal to 0.3:

random.geometric(p=0.3, size=10)

import unittest

class TestingGeometric(unittest.TestCase):
  def test_within_range(self):
    result = random.geometric(p=0.3, size=10)
    print(result)
    is_within_range = len(result) ==10
    self.assertTrue(is_within_range)

#sample output:
#array([3, 1, 1, 9, 1, 7, 1, 2, 1, 6])
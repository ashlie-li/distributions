#The gamma distribution is a family of right-skewed, continuous probability distributions. These distributions are useful in real-life where something has a natural minimum of 0.
#the probability density function is:
#Γ(α) = the intergral of y**(α−1)*e**(−y)dy from 0 to inf.

from numpy import random
random.gamma(shape=0, scale=1.0, size=None)

#example:
shape, scale = 2., 2.  # mean=4, std=2*sqrt(2)
result = random.gamma(shape, scale, 10)
print(result)

import unittest

class TestingGamma(unittest.TestCase):
  def test_within_range(self):
    result = random.gamma(shape, scale, 10)
    print(result)
    is_within_range = len(result) ==10
    self.assertTrue(is_within_range)

#sample output:
# [2.39723016  1.5582142   3.2330635  13.41448232  3.84578816  3.48312361, 4.20523677  6.11990912  1.38563777  7.51076888]
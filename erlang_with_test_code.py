#The Erlang distribution is a specific case of the Gamma distribution. It is defined by two parameters, k and μ,
# The probability density function is: f(x) = (x**(k-1) * e**(-x/μ))/(μ**k * (k-1)) for x >0
#where k is the shape parameter and μ is the scale parameter.

import numpy as np


from scipy.stats import erlang
numargs = erlang.numargs
[a] = [0.6, ] * numargs
R = erlang.rvs(a, scale = 2,  size = 10)
print ("Random Variates : \n", R)

import unittest

class TestingErlang(unittest.TestCase):
  def test_within_range(self):
    result = erlang.rvs(a, scale = 2,  size = 10)
    print(result)
    is_within_range = len(result) ==10
    self.assertTrue(is_within_range)





#Poisson distribution can be used to show how many times an event is likely to occur within a specified period of time.
#the formula is f(x) = (λ**x)*(e**(-λ))/(x!)
#e: Euler's number (e = 2.71828...)
#x: the number of occurrences
#x!: the factorial of x
#λ: the expected value of x when that is also equal to its variance.

from numpy import random

random.poisson(lam=1.0, size=None)

#example: generate a sample of poisson random variables with λ=5, size = 500.

random.poisson(5, 20)

import unittest

class TestingPoisson(unittest.TestCase):
  def test_within_range(self):
    result = random.poisson(5, 20)
    print(result)
    is_within_range = len(result) ==10
    self.assertTrue(is_within_range)

#sample output:
#array([6, 4, 5, 6, 3, 7, 6, 6, 3, 8, 8, 3, 5, 3, 7, 5, 6, 6, 5, 5])

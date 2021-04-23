#A uniform distribution, also called a rectangular distribution, is a probability distribution that has constant probability.
#The probability density function of the continuous uniform distribution is: f(x) =1/(b-a) for a <= x <= b, f(x) = 0 for x <a or x > b
#a is the minimum and b is the maximum of x.

from numpy import random
random.uniform(low=0.0, high=1.0, size=None)

#example: generate a 5X2 matrix with the values of the vectors are between 0 and 1.


import unittest

class TestingUnifrom(unittest.TestCase):
  def test_within_range(self):
    result = random.uniform(0.0, 1.0, size = (5,2))
    print(result)
    is_within_range = all(i >= 0.0 and i <= 1.0 for i in result.flatten())
    self.assertTrue(is_within_range)

unittest.main()
#sample output:
# array([[0.85579158, 0.92836813],
#       [0.04551638, 0.87683327],
#       [0.82121348, 0.47738449],
#       [0.74072852, 0.49908354],
#       [0.8319029 , 0.37512834]])
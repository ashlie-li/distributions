#A triangular distribution is a continuous probability distribution shaped like a triangle.
#The probability density function is:
#f(x) = o for x <a,
#f(x) = 2*(x-a)/((b-a)*(c-a)) for a <= x <= c,
#f(x) = 2*(b-x)/((b-a)*(b-c)) for c<= x <= b,
#f(x) = 0 for x>b

#where:
# a: the minimum value, where a ≤ c,
# c: the peak value (the height of the triangle), where a ≤ c ≤ b,
# b: the maximum value, where b ≥ c.

from numpy import random
random.triangular(left=-1, mode=0, right=1, size=None)

#example: generate a group of 30 random variables using triangular distribution with a minimum value to be -5, the peak value at 0 and the maximum value to be 5.

random.triangular(-5, 0, 5, 30)

import unittest

class TestingTriangular(unittest.TestCase):
  def test_within_range(self):
    result = random.triangular(-5, 0, 5, 30)
    print(result)
    is_within_range = all(i >= -5 and i <= 5 for i in result)
    self.assertTrue(is_within_range)

#sample output
#array([-2.25631129, -0.22543387, -0.98729561,  0.89223229,  0.101949  ,
        # 1.80172198, -4.23302647,  1.4538379 ,  0.4269142 , -3.09030751,
        # 0.69488861,  4.42860228, -1.20539004, -1.7300038 , -0.40113604,
        # 2.74335322, -0.64933984,  1.56717144, -0.26733617, -2.68407694,
        # 1.07806457,  3.53224179,  0.53899215, -2.72005853,  2.98766588,
        # 1.16438291,  1.89468396,  0.40356427,  1.40376679,  1.88390749])

#plot a group of triangular random variables in a plot.

import matplotlib.pyplot as plt
result = random.triangular(-5, 0, 5, 500)
plt.hist(result, bins = 50, density = True)
plt.show()


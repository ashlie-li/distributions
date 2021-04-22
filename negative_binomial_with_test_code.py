#Negative binomial distribution describes a sequence of i.i.d. Bernoulli trials, repeated until a predefined, non-random number of successes occurs.
#The probability formula: b(x; r, P) = x-1Cr-1 * P**r * (1 – P)**(x – r)
#where: where
# x=number of trials required to produce r successes
# r = Successes
#p = the probability of success

from numpy import random
np.random.negative_binomial(n, p, size=None)

#example: A company drills oil exploration wells, each with an estimated probability of success of 0.1. generate the random varaibles of how many drills can be taken for 1 success in 10 tails.

np.random.negative_binomial(n=1, p=0.1, size=10)

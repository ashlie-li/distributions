#A Bernoulli distribution is a discrete probability distribution with two possible outcomes: either success or failure. Success happens with probability p, while failure happens with probability 1-p.
# The probability density function (pdf) for this distribution is p**x*(1 – p)**1 – x, which can also be written as: P(n) = p for n = 1 and p(n) = 1-p for n = 0.

import numpy as np

def bern(p,size=1):
    rvs = np.array([])
    for i in range(0,size):
        if np.random.rand() <= p:
            a=1
            rvs = np.append(rvs,a)
        else:
            a=0
            rvs = np.append(rvs,a)
    return rvs

    #test example: Tossing a coin. generate the random variate 10 times to see how many head(1) and how many tail(0) occur.

  bern(0.5, 10)
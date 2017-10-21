import math
import numpy as np
from collections import Counter

class FeatureTargetBond:
    """
    Class for further reference.

    """

    def __init__(self, x, t):
        self.x = x
        self.t = t

    def __eq__(self, o):
        if (self.x == o.x):
            return True
        else:
            return False

    def __ne__(self, o):
        if (self.x != o.x):
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.x, self.t))

    def __str__(self):
        return "({0},{1})".format(self.x, self.t)


def shannon_entropy(x):
    """
    Calcualtes the Shannon Entropy
    for array x.

    :param x:
    :return:
    """
    t = len(x)
    c = Counter(x)

    # Get the frequencies for each element in x.
    c = c.most_common()

    # Calculate the probabilities.
    p = [c[i][1]/t for i in range(len(c))]
    h = -1.0*sum([p[i]*math.log2(p[i]) for i in range(len(p))])

    return h


def remaining_entropy(ft):
    """
    Calcualtes the remaining entropy
    after the feature split with respect to
    the targets.

    :param ft: N x 2 array. First column - feature,
                            Second column - targets.
    :return:
    """

    n = len(ft)

    f = ft[:, 0]
    uf = np.unique(f)

    rh = 0.0
    for i in range(len(uf)):
        pf = ft[f == uf[i]]
        h = (len(pf)/n)*shannon_entropy(pf[:, 1])
        rh = rh + h

    return rh



if __name__ == "__main__":

    ft = [[0, 1],
          [1, 1],
          [1, 1],
          [1, 0],
          [0, 0],
          [0, 0]]

    """
    ft = [[1, 1],
          [0, 1],
          [0, 1],
          [1, 0],
          [0, 0],
          [0, 0]]
    """

    ft = [[1, 1],
          [1, 1],
          [1, 1],
          [0, 0],
          [0, 0],
          [0, 0]]


    ft = np.array(ft)
    h = shannon_entropy(ft[:, 1])
    rh = remaining_entropy(ft)
    print(h)
    print(rh)
    print(h - rh)


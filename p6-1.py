import math
import numpy as np

# E = math.e

ly1Outs = [[4.8, 1.21, 2.385],
           [8.9, -1.81, 0.2],
           [1.41, 1.051, 0.026]]

expValues = np.exp(ly1Outs)

normValues = expValues / np.sum(expValues, axis=1, keepdims=True)
print(normValues)

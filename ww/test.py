# Ваше решение
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]], float)
# >>>
a[1,:]
# array([ 4.,  5.,  6.])
# >>> 
a[:,2]
# array([ 3.,  6.])
# >>> 
a[-1:, -2:]
# array([[ 5.,  6.]])



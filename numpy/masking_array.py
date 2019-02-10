import numpy as np
import random

arr = np.arange(30).reshape(5,6)
mask = arr > 10
print "Mask is: ",mask

#Applying the mask on original array
print sum(arr[mask])
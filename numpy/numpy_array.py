
import time,sys
import numpy as np
#numpy array is much faster than python list

lst1 = range(1000000)
lst2 = range(1000000)

start = time.time()
resultList = map(lambda x,y: x+y,lst1,lst2)

print("Total time taken for adding two python lists: ", (time.time() - start)*1000)


npArray1 = np.arange(1000000)
npArray2 = np.arange(1000000)
start = time.time()
print("Total time taken for adding two numpy arrays: ", (time.time() - start)*1000)


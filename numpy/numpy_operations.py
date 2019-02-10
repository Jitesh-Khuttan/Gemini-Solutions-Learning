import numpy as np

single_array = np.array([1,2,3,4,5,6])

two_array = np.array([[1,2,3],
                      [4,5,6],
                      [7,8,9]
                      ],dtype = 'float64')

#Check the datatype of the array
print "Dtype of single: ",single_array.dtype
print "Dtype of two: ",two_array.dtype

#Check the dimension of the array
print "Dimension of single: ", single_array.ndim
print "Dimension of two: ", two_array.ndim

#Check the size of the type_of element in array
print "Item Size of one: ",single_array.itemsize
print "Item Size of two: ",two_array.itemsize

#Check the number of elements in an array
print "Number of elements in one: ",single_array.size
print "Number of elements in two: ",two_array.size

#Check the dimension (shape) of the n-D array (rows,columns)
print "Shape of one: ",single_array.shape
print "Shappe of two: ",two_array.shape

#Create a new np Array with zeroes
zeros_array = np.zeros( (5,5) )
ones_array  = np.ones( (3,3) )
print zeros_array
print ones_array

#Create an array with linear spacing
lin_array = np.linspace(1,10,6)
print "Linearly Spaced Array: ", lin_array


#Change the dimension(shape) of the array
reshaped_array = single_array.reshape( (2,3) )
print(reshaped_array)

#Flatten n-D array to 1-D array
print two_array.ravel()


#Finding the minimum and maximum of the array
print "Maximum of 2-d array:", two_array.max()
print "Minimum of 2-d array:",two_array.min()

#Find sum along columns
print "Sum along columns: ", two_array.sum(axis=0)

#Find sum along rows
print "Sum along rows: ",two_array.sum(axis=1)

#Calculate the square_root and standard deviation of the array
np.sqrt(two_array)


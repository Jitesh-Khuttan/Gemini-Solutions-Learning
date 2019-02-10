import numpy as np

arr1 = np.arange(30).reshape(2,15)
arr2 = np.arange(31,61).reshape(2,15)

#Stacking the arrays horizontally
print("Stacking Horizontally")
harr_12 = np.hstack( (arr1,arr2) )
print harr_12

#Stacking the array vertically
print("Stacking Vertically")
varr_12 = np.vstack( (arr1,arr2) )
print varr_12

#Splitting the array horizontally
print("Splitting Horizontally")
hsarr_12 = np.hsplit(arr1,3)
print hsarr_12

#Splitting the array Vertically
print ("Splitting Vertically")
vsarr_12 = np.vsplit(arr1,2)
print vsarr_12
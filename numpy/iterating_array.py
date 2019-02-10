import numpy as np

arr_1 = np.array([1,2,3,4,5])
arr_2 = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]
                  ])

arr_3 = np.array([
    [
        [1,2,3],[4,5,6],[7,8,9]
    ],
    [
        [10,11,12],[13,14,15],[16,17,18]
    ]
])

print ("Iterating 1-D array")
for element in arr_1:
    print element,

print ("\nIterating 2-D array as rows")
for row in arr_2:
    print row

print ("Iterating 2-D array as elements")
for row in arr_2:
    for element in row:
        print element,
    print

print ("Iterating 2-D array by flattening it")
for element in arr_2.flat:
    print element,

print ("\nIterating 3-D array as 2-D arrays")
for d_2 in arr_3:
    print d_2

print ("Iterating 3-D array as elements")
for d_2 in arr_3:
    for row in d_2:
        for element in row:
            print element,
        print
    print
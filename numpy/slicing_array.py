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

print ("1-D array is: ",arr_1)
print ("2-D array is: ",arr_2)
print ("3-D array is: ",arr_3)

print ("Slicing 1-D array")
#[start_index : end_index+1]
print (arr_1[2:4])

print ("Slicing 2-D Array")
#[start_row_index : end_row_index+1 , start_col_index : end_col_index + 1]
print (arr_2[:,1:3])

print ("Slicing 3-D Array")
#[start_2D_array_index : end_2D_array_index+1,start_row_index : end_row_index+1 , start_col_index : end_col_index + 1]
print(arr_3[:,:,-1])
print(arr_3[0,0:2,-1])
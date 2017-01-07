import numpy as np

# input list
a = [[1,2,3],[4,5,6]]

# convert to numpy array
b = np.array(a, float)

# number of dimensions => 2
print(b.ndim)

# number of rows and columns  => (2,3)
print(b.shape)

#data type => float64
print(b.dtype)

# Slicing operations

# : in first argument means do this on all dimensions => [1,2],[4,5]
print(b[:, 0:2])

# slicing along specific direction => [4,5]
print(b[1,0:2])

# reshape => total size (m*n) should not change. So 2*3 in the above example can be 3*2 or 6*1.
c = b.reshape((3,2))
print(c)

#transpose
print(c.transpose())

#flatten multi dimensional array to 1d
print(c.flatten())

#concatenate. Join 2 or more arrays
# if one of the arrays is multi dimensional, we can specifiy the axis along which the concatentaion should happen
array1 = np.array([[1,2],[3,4]], float)
array2 = np.array([[5,6],[7,8]], float)

array3 = np.concatenate((array1, array2))
print(array3)

array3 = np.concatenate((array1,array2),axis=1)
print(array3)
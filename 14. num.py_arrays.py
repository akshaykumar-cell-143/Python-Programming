# Numpy:
# Numpy(Numerical python) is a python library used for scientific and mathematical computing.
# It provides:
# -> Powerfull array objects(more effective than python lists.)
# -> Vectorized operations (Fast element-wise calculations.)
# -> Support for linear algebra, statistics,Random numbers operations etc...
# importing the numpy librabry.
# import numpy as np
# aa = np.array([1,2,3])
# print(aa)  # [1,2,3]

# import array as arr
# Creating an array with numpy:
# Array = arr.array('i',[1,2,3,4,4,7])
# 1D Array:
# A1D = np.array([1,2,3,4,5])
# print(A1D)
# 2D Array:
# A2D = np.array([[1,2,3],[4,5,6],[7,8,9]])
#[
#   1 2 3
#   4 5 6
#    7 8 9
#]
# print(A2D)

# Methods and Operations in Numpy Arrays:
# 1. Basic Array Information methods:
# A = np.array([1,2,3,4,5])
# ndim: Returns the number of dimensions of the array.
# print(A.ndim)  # 1
# print(A2D.ndim) # 1
# Shape: Returns a tuple showing the sizes of the array in each dimensions(rows,columns,etc..)
# print(A2D.shape)  # (3,3)
# Size: Returns the total number of elements in the array.
# print(A2D.size) # 9 =  len
# dtype: Returns the datatype of the elements in the array.
# print(A2D.dtype) # int64 = type
# import numpy as np
# 2. Creating an array with numpy:
# Zeros: Creats an array  of 6 zeros.
# print(np.zeros(6)) # 0 0 0 0 0 0 
# ones: Creats an array of 6 ones.
# print(np.ones(1)) # 1
# Arange(): creates an array with a range of values.
# print(np.arange(1,11,1)) # [1 2 3 4 5 6 7 8 9 10]
# print(np.arange(0,11,2)) # [0 2 4 6 8 10]
# print(np.arange(1,11,2)) # [1,3,5,7,9]
# linspace: Creates 3 numbers evenly spaced between 0 and 1.
# print(np.linspace(0,1,3)) # [0,0.5,1]

# Mathematical operations:
# A = np.array([1,2,3,4,5])
# L = [1,2,3,4,5]
# print(A+6)  # [7 8 9 10 11]
# AA = []
# for i in A:
#     AA.append(i+6)
# print(AA) # [np.int64(7),np.int64(8),np.int64(9),np.int64(10),np.int64(11)]
# print(A-1) # [0,1,2,3,4]
# print(A*2) # [2,4,6,8,10]
# print(A/2) # [0.5,1,1.5,2,2.5]
# print(A//2) # [0,1,1,2,2]
# print(A**6) # [1,64,729,4096,15625]

# Aggregate Functions:
# A = np.array([1,2,3,4,5])
# sum():
# print(np.sum(A)) # 15
# mean():
# print(np.mean(A)) # 3
# max():
# print(np.max(A)) # 5
# min():
# print(np.min(A)) # 1
# median():
# print(np.median(A)) # 3
# std:
# print(np.std(A)) # 1.41421
# cumprod:
# print(np.cumprod(A)) # [1,2,6,24,120]

# Matrix Operations:
# Mat1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
#[
#    1 2 3
#    4 5 6 
#    7 8 9
#]
# Mat2 = np.array([[9,8,7],[6,5,4],[3,2,1]])
#[
#    9 8 7
#    6 5 4 
#    3 2 1
#]
# print(Mat1+Mat2)
# print(Mat1**2)
# print(Mat1*Mat2)
# dot():
# print(np.dot(Mat1,Mat2))
# Transpose:
# print(np.transpose(Mat1))
# print(np.transpose(Mat2))
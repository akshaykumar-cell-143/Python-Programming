# Arrays in Python:
# An Array is collection of elements of the same datatype stored in a continuous memory location.
# Arrays are used to store multiple values in a single variable.
# Why Arrays?
# Easy to manage multiple values.
# Allows Faster operations like searching and sorting.
# Useful in mathematica and scientific problems.
# Saves memory.
# Array VS Lists:
# Importing the array module.
import array as arr

# Creating an array:-
Numbers = arr.array('i',[1,2,3,4,5])
print(type(Numbers))  # <class 'array.array'>
print(Numbers)  # array('i', [1,2,3,4,5])
# i = Integer
# f = Float
# u = String

# Accessing Array Elements:-
Numbers = arr.array('i',[1,2,3,4,5])
#                         0 1 2 3 4 

print(Numbers[0]) # 1
print(Numbers[1]) # 2
print(Numbers[2]) # 3
print(Numbers[3]) # 4
print(Numbers[4]) # 5

# Adding An element in Array:-
# Append():
Numbers.append(7)
print(Numbers)
# insert():
Numbers.insert(2,6)
print(Numbers)
# Extend():
Numbers.extend([8,9])
print(Numbers)
# Deleting an element:
Numbers.remove(3)
print(Numbers)
#pop():
Numbers.pop(2)
print(Numbers)
# Clear():
Numbers.clear()
print(Numbers)
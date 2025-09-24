# Sets:-
# Set is a collection datatype which is used to store the multiple values in a single variable.
# Sets are unordered,unindexed,mutable, and they do not allow duplicate values.
# They are useful when you want to store unique elements and performs the mathematical,
# operations like union, intersection , and difference.
# Syntax:-
# My_set = {element1,element2,element3}
# Characteristics of Sets:-
# Unordered:-
# Example:- {1,2,3} and {3,2,1} are considered the same set.
# Unindexed:- You cannot access set elements by the index like lists or tuples. set[1]
# a = {1,2,3}
# print (a[1])
# Unique values only:- Duplicate values are automatically removed from the set.
a = {1,2,3,3,2,1,1,1,2}
print(a) # output {1,2,3}

# Creating a set:-
s1 = {1,2,3}
s2 = {10,12.5,"Hello",True}

# Empty set:-
s31 = {}
s3 = set()
print(type(s3)) # <class 'set'>
print(type(s31)) # <class 'dict'>

# Accessing sets:-
# We cannot directly access an element using index but we access an element using loops.
A = {"Rajinikanth","Snake king","Upendra"}
for role in A:
    print(role)

# Adding an element in sets:-
S = {12,18,20}
S.add(25) # adds only single element in any position.
S.update([34,29]) # adds the multiple values in the set.
print(S)  # {34,12,18,20,25,29}
# Deleting the elements in set:-
# Remove():- Removes the element, but it gives an error if the values is not found in the set.
S.remove(25)
print(S)  # {34,12,18,20,29}
# Discard:- Removes the element, but it gives no error if the values is not found in the set.
S = {34,12,18,20,25,29}
S.discard(26)
print(S) # {34,18,20,25,12,29}

# Pop():- Removes the random element from the set.
S = {34,12,18,20,25,29}
S.pop()
print(S)  # {18,20,25,12,29}

# Clear():- Removes the every element from the set.
S = {34,12,18,20,25,29}
S.clear()
print(S)  # set()

# Mathematical operations in set:-
# Union "U"="|": Prints all unique values or elements from the both sets.
A = {1,2,3}
B = {4,5,6}
print(A|B)  # {1,2,3,4,5,6}
# Intersection: "n" = "&" :
A = {1,2,3,4}
B = {3,4,5,6}
print(A & B)  # {3,4}

# Difference: "-" = "-" : removes the common elements from the lists but prints only the first sets values.
A = {1,2,3,4,5,6}
B = {1,2,3,6,7,8}
print(A-B)  # {4,5}

A = {1,2,3,4,5,6}
B = {1,2,3,6,7,8}
print(B-A)  # {8,7}
 
# Symmetric Difference:- "^" :
# removes the common elements from the lists but prints only the first sets values.
A = {1,2,3,4,5,6}
B = {1,2,3,6,7,8}
print(A ^ B)  # {1,2,5,6}

# Mathematical operations using functions:-
A = {1,2,3,4,5,6}
B = {1,2,3,6,7,8}
# Union:
print(A.union(B))  # {1,2,3,4,5,6,7,8}
# Intersection:
print(A.intersection(B))  # {1,2,3,6}
# Difference:
print(A.difference(B))  # {4,5}
# Symmetric difference:
print(A.symmetric_difference(B))  # {4,5,7,8}

# len():
S = {1,2,3,4,5,6}
print(len(S))  # 6
# max():
S = {1,2,3,4,5,6}
print(max(S))  # 6
# min():
S = {1,2,3,4,5,6}
print(min(S))  # 1
# sum():
S = {1,2,3,4,5,6}
print(sum(S))  # 21
# Sort():
numbers = {2,5,3,1,6,8,4,9}
print(numbers)
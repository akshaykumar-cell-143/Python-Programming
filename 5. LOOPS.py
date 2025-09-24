#Loop is a program
#for variable in seq:
#  code block
#range(start v(0),end v, step v)
for i in range(10):
    print(i)
else:
    print("Done")
for i in range(1,5,1):
    print("Hello")
#Print the numbers from 9 to 27:
for i in range(9,28):
    print(i)
#Using default values print the numbers upto 15.
for i in range(16):
    print(i)    
for i in range(11,1,-1):
    print(i)
# Print the even numbers from 0 to 20
for i in range(0,21,2):
    print(i)
# Print squares of a number upto 6 
for i in range(6):
    print(i**2)

fruits = ["apple","mango","banana"]
for fruit in fruits:
    print(fruit)
#5 table:
for i in range(1,11):
    print("5 X", i, "=", 5*i)

#7 table:
for i in range(1,11):
    print("7 X", i, "=", 7*i)

# 1+2+3+4+5+6+7+............+25 = ?
sum = 0
for i in range(1,26):
    sum += i
print(sum)
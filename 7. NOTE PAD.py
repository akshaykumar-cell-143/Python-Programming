--->KEYWORDS:-
it is also known as reserved words.

if,else,print,
for,elif,while,
list,tuple,set,
int,float,input.

-->RULES TO WRITE VARIABLES :-
1.Donot starts with 12(numbers)
try to use $,_eg:roll_no
try to write camelcase
      eg:nameAkshay

#-->NOTE:-using,
name="akshay"
name1="kumar"
print(name , name1)--->output is (akshay kumar)

#concatenation:-
it adds a string (+)
name="AKSHAY"
name1="KUMAR"
print(name + name1)-->output is AKSHAYKUMAR
print(name+" "+name1)-->output is AKSHAY KUMAR
#CONDITIONAL STATEMENT:-
->In conditional statement it contains certain statements,
that statement executes based on coditions.
->the condition is true it executes.
#TYPES OF CONDITIONAL STATEMENTS;-
<>if
<>if-else
<>elif
<>nested if

1.<>if:-
syntax
if cond:-
    #Statements
->If condition is true then the statements gets executes.
x=10
if x>9:
    print("yes x is greater than 5")-->output is "yes x is greatewr than 5"
x=20
if x<21:
    print("yes x is greater than 5")-->output is "yes x is greater than 5"

2.<>if-else:-
->if IF is true(cond) then it executes if block statements
->if IF condition is false then it executes else block statement.

x=10
if x>20:
    print("yes x is greaTER THAN 5")-->output is "not valid"
else:
    print("not valid")
if x<20:
    print("yes x is greater than 5")-->output is "yes x is greater than 5"
else:
    print("not valid")

3.<>elif:-
 x=10
if x>20:
    print("cond1")
elif x>5:
    print("cond2")
elif x>7:
    print("cond3")
else:
    print("not valid")

 output is "cond2"

#print is used for display the output in our program
print("Hello World!")
#Bio - Data
print("Name: Akshay")
print("Age: 18")
print("Branch: CSE-Ai&Ml")
print("Place: Siddipet")
print("College: MRCET")
#Bio-Data Using input and ouput statements
Name=input("Enter your name: ")
Age=input("Enter your age: ")
Branch=input("Enter your branch: ")
place=input("Enter your place: ")
College=input("Enter your college name: ")
print("Name: ",Name)
print("Age: ",Age)
print("Branch: ",Branch)
print("Place: ",place)
print("College: ",College)

#BITWISE OPERATOR:-
    0 1 2 4 8 16 32 64
--|--------------------
0 | 0 0 0 0 0
1 | 0 1 0 0 0
2 | 0 0 1 0 0
3 | 0 1 1 0 0
4 | 0 0 0 1 0
5 | 0 1 0 1 0
6 | 0 0 1 1 0
7 | 0 1 1 1 0
8 | 0 0 0 0 1
9 | 0 1 0 0 1
10| 0 0 1 0 1
11| 0 1 1 0 1
12| 0 0 0 1 1

5 & 3  ---> AND
5 | 3  ---> OR
5 ~ 3  ---> NOT
5 ^ 3  ---> XOR
5 << 3 ---> LEFT SHIFT
5 >> 3 ---> RIGHT SHIFT

x1=5
y1=3
print(x1 & y1)
print(x1 | y1)
print(~x1)
print(x1 ^ y1)
print(x1 << y1)
print(x1 >> y1)

#LOOPS CONTENT STATEMENT:-

->Loop is a programming content that allows us to repeat a
 set of instructions multiple times without writing them again
 and again.Instead of repeating the same code, we use a loop to
 make the computer do the task repeatedly until a certain
 condition is met.

->in programming,a loop is used when we want to repeat a set of
  instructions multiple times without writing the code again and
  again.

# ITERATION:-

->Iteration means one complete execution of the loop body.
  in simple words,each time the loop runs,it is called one iteration.
  if a loop runs 5 times,it means the loop has 5 iterations.
# TYPES OF LOOPS IN PYTHON:-

In python, there are mainly two types of loops:-

1.For loop->Used when the number of repetitions is known.

1.FOR LOOP:-

-> A for loop is a type of loop that repeats a block of code
   for a specefic number of times.it is mostly used when we
   know how many times we want to repeat something.
-> It automatically goes through to one by one.

#SYNTAX:-

for variable in sequence:

    #code to be executed

    . variable->tales each value from the sequence one by one.
    
    . sequence->can be a range of numbers,list,string,or any
      iterable object.
      
    . Indenation(space) is very important in python.  

WHY DO WE USE FOR LOOP?

1. To avoid repetition of code.

2. To process collections of data(like going through all
       numbers in list,or letters in a string).

3. To perform actions a fixed number of times.

#COLLECTION DATA TYPES:-
list1 = [10,20,30,40,50]
-> This collection datatypes also known as non primitive data types.
-> This collection datatypes are used to store multiple values in single variables.

#Types of collection datatypes in python:-
1.Lists.
2.Tuples.
3.Sets.
4.Dictionary.

1.Lists in python:-
-> Lists are a collection datatypes which are used to store multiple 
   values in a variable.
-> Lists are ordered( the items have a fixed position) and mutable
   ( we can change, add or remove items from the list).
#Example:-
list1 = [10,20,30,40,50]               #Integers values
fruits = ["apple","banana","mango"]    #Strings values
list2 = [10.1,20.2,30.3,40.4,50.5]     #Float values
list3 = [True,False,True,True]         #Boolean values
list4 = [10,20.5,"hello",True,"False"] #Multi data types

#Accessing Elements:-
->Accessing elements are used to retrive the list items or values stored
  at a particular position (index - indexs are starts from zero)
#index - In python, every element in a list is stored with a positive numbers
 called as index.
#Example:-0,1,2,3,4,5,6,......,n-1
list1 = [10,20,30,40,50]
print(list1[0])#10
print(list1[1])#20
print(list1[2])#30
print(list1[3])#40
print(list1[4])#50
#By negative values:-
print(list1[-1])#50
print(list1[-2])#40
print(list1[-3])#30
print(list1[-4])#20
print(list1[-5])#10   

#Slicing in lists:-
-> Slicing is taking out of a part from the main list.
-> Slicing will extracts the part or sublist using [start idx : end idx].
#example:-
s1c1 = ["Prabhas","Balayya","Pspk","BOB","Bhai"]
print(s1c1[:3])
print(s1c1[1:4])
print(s1c1[-3:])
#Adding elements in list:-
We can add new values to a list in different ways:-
1. Append.
2. Insert.
3. Extending.
# 1. Append : Adds a single value at the end of the list.
kalkicast = ["Prabhas","Kamal hasan","Amitha Bhachan","Deepika p","SSR"]
kalkicast.append("Deesha patani")
print(kalkicast)
# 2. Insert : Adds a single value at particular place of the list.
kalkicast = ["Prabhas","Kamal hasan","Amitha Bhachan","Deepika p","SSR"]
kalkicast.insert(5, "Deesha patani")
print(kalkicast)
# 3. Extending : Adds multiple values at once by combining the lists.
kalkicast = ["Prabhas","Kamal hasan","Amitha Bhachan","Deepika p","SSR"]
kalkicast.extend(["Anudeep","Mrunal T","Bujji"])
print(kalkicast)

#Removing Elements in list:-
Removes the items in the list in different ways.
1. remove():
2. pop():
3. clear():
# 1. remove():
fruits = ["apple","banana","mango"]
fruits.remove("apple")
print(fruits)
# 2. pop():
fruits = ["apple","banana","mango"]
fruits.pop(2)
print(fruits)
# 3. clear():
fruits = ["apple","banana","mango"]
fruits.clear()
print(fruits)

# Changing The Elements:-
-> Lists are mutable, we can change the values after creating the lists using index.
fruits = ["apple","banana","mango"]
fruits[1] = "watermelon"
print(fruits)
-> This changing is mainly used for replace a data in the list.
-> i.e; replace the "watermelon" with "banana".

# Mathematical Operations in Lists:- 
1. Concatenation: Joins the two lists together in one list.
a = [1,2]
b = [3,4]
c = a+b
print(c)
2. Repetition: Repeats the elements of a list multiple times.
a = [1,2]
n = int(input("Enter the n value:"))
b = a*n
print(b)

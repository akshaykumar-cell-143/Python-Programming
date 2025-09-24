# Arithematic operator
a=10
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
# comparision operator
x=5
y=5
print(x==y)
print(x!=y)
print(x>y)
print(x>=y)
print(x<=y)

#LOGICAL OPERATOR:-
#AND:-
p=5
q=10
print(p>2 and q>5)
print(p>2 and q<5)
print(p<2 and q>5)
print(p<2 and q<5)
#OR:-
p1=5
q1=10
print(p1>2 or q1>5)
print(p1>2 or q1<5)
print(p1<2 or q1>5)
print(p1<2 or q1<5)
#NOT:-
p2=5
q2=0
print(not(p2))
print(not(q2))

#BITWISE OPERATOR:-
x1=5
y1=3
print(x1 & y1)
print(x1 | y1)
print(~x1)
print(x1 ^ y1)
print(x1 << y1)
print(x1 >> y1)

#IDENTITY OPERATOR:-
x = [1,2,3,4]
y = x
z = [1,2,3,4]
print(x is y) # output is "True"
print(x is z) # output is "False"
print(x is not z) # output is "True"

#MEMBERSHIP OPERATOR:-
text = "Akshay"
print("Ak" in text) # output is "True"
text = [1,2,3,4]
print(4 in text) # output is "True"
print(4 not in text) # output is "False"
print(5 not in text) # output is "True"

# AREA OF CIRCLE:= pi*r*r
r = int(input("Enter r value:"))
Area_of_circle = 3.14*2*2
print(Area_of_circle)
#output is "12.56"
r= float(input("Enter r value:"))
print(Area_of_circle)
#output is "12.56"

#AREA OF TRIANGLE:-
height = int(input("Enter the height value: "))
base = int(input("Enter the base value: "))
AOT = 0.5*height*base
print(AOT)

#FINDING SQUARE AND CUBE OF A NUMBER:-
a = int(input("Enter a number: "))
sqe = a*a
cube = a*a*a
print("Square of",a,"is: ",sqe)
print("cube of",a,"is: ",cube)

#km -> m, m -> cm,
dis = 25#m
km = dis/1000
print(km)  # output is "0.025"
m = dis*1000
print(m)  # output is "25000"
m1 = dis/100
print(m1)  # output is "0.25"
cm = dis*100
print(cm)  # output is "2500"
miles = dis*1.6
print(miles)  # output is "40.0"

# FIND THE NUMBER IS EVEN OR ODD:-
#Even = 0,2,4,6,8,10,........
#ODD = 1,3,5,7,9,..........
num = int(input("Enter number: "))
if num%2==0:
    print("Number is even")
else :
    print("Number is odd")
    
# LEAP YEAR OR NOT :-
year = int(input("Enter the year: "))
if (year%4==0 and year%100!=0) or year%400==0:
   print("It is a leap year.")
else:
    print("It's not a leap year.")
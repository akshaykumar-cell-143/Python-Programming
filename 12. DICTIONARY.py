# Dictionary:-
# Dictionary is a in-built datatype, which is used to store multiple values in a 
# single variable.
# Dictionary stores the data in the form of key-values pairs.
# Each key is unique and works as an index to access its corresponding value.
# Keys are immutable(can't be changed once created),while values can be anything(mutable).
# Dictionary are: Ordered(from python 3.7+ version), Mutable,Do not allows the duplicate keys.
# Syntax:
My_dict = {

    "key1":"value1",
    "key2":"value2",
    "key3":"value3",
    "key4":"value4"
}
print(My_dict)  
# Characteristics of Dictionatry:
# Key-value pairs:
# Every entry of Dictionary's element is a pair:
# keys and values.
# { "name":"Akshay"}
# Unique keys:
# example:
A = {"n":"Akshay","n":"Anurag"}
print(A) # "n1":"Anurag"
# Keys must be immutable:
# keys can be(valid keys):integer,float,string
My_dict = {
    1:"value1",
    10.2:"value2",
    "key3":"value3",
    "key4":"value4"
}
print(My_dict)    

# Creating Dictionary:
# Normal Dictionary:
BioData = {
    "Name":"Akshay",
    "Roll.No":"5M3",
    "Branch": "CSE-AI&ML",
    "place":"Siddipet"
}    
print(BioData)

# Dictionary using constructor:
BioData1 = dict( Name="Akshay", RollNo="5M3", Branch="CSE-AI&ML", Place="Siddipet")
print(BioData)                          
# Empty Dictionary:
E_D = {}

# Accessing the Dictionary:
# -> To access an element we use key names inside the square brackets[] or we can use get() method.
BioData = {
    "Name":"Akshay",
    "Roll.No":"5M3",
    "Branch": "CSE-AI&ML",
    "place":"Siddipet"
}    
print(BioData)
# Square brackets []
print(BioData["Name"]) # Anurag
print(BioData["Roll.No"]) # 5M3
print(BioData["Branch"])  # CSE-AI&ML
print(BioData["place"])   # Siddipet
# print(BioData["age"]) # keyerror(because the "age" is not created in dictionary)

# Using get() method:
print(BioData.get("Name")) # Anurag
print(BioData.get("Roll.No")) # 5M3
print(BioData.get("Branch"))  # CSE-AI&ML
print(BioData.get("place"))   # Siddipet
print(BioData.get("age")) # None instead of error

# Adding and Updating Dictionary:
# Adding: You can insert a new key-value pair into a dictionary.
# Updating: You can update or change the values using exsisted keys in the dictionary.
BioData = {
    "Name":"Akshay",
    "Roll.No":"5M3",
    "Branch": "CSE-AI&ML",
    "place":"Siddipet"
}    
BioData["age"] = 18  # Adding the new key and values
print(BioData)
BioData["place"] = "Hyderabad" # changing or updating the exsisted key's value.
print(BioData)

# Removing in Dictionary:
# python gives multiple ways to delete items from a dictionary.
# pop(),popitem(),clear(),del(delete)
BioData = {
    "Name":"Akshay",
    "Roll.No":"5M3",
    "Branch": "CSE-AI&ML",
    "place":"Siddipet",
    "Role":"siddipet_don"
}
print(BioData)
# pop(): Removes the key value
BioData .pop("Roll.No")
print(BioData)
# popitem(): Remove the last inserted item from the dictionary.
BioData.popitem()
print(BioData)
# del(delete): deletes the key from the dictionary.
del BioData["Branch"]
print(BioData)
# Clear(): removes every item from the dictionary.
BioData.clear()
print(BioData)

# Dictionary methods:
# Methods allow you to access dictionary data easily.
# Key(),values(), items()
BioData = {
    "Name":"Akshay",
    "Roll.No":"5M3",
    "Branch": "CSE-AI&ML",
    "place":"Siddipet",
    "Role":"siddipet_don"
}
# Keys(): It prints only the keys of dictionary.
print(BioData.keys())
# Values(): It prints only the values of dictionary.
print(BioData.values())
# Items(): It prints only the items of dictionary.
print(BioData.items())

# Updating update(): update the multiple values 
BioData.update({"Role":"Web Developer","Place":"Hyderabad"})
print(BioData)

# loops for dictionary:
for i in BioData:
    print(i)
    
L = [10,20,30,40,50]
for i in range(0,5):
    print(L[i])

BioData = {
    "Name":"Akshay",
    "Roll.No":"5M3",
    "Branch": "CSE-AI&ML",
    "place":"Siddipet",
    "Role":"siddipet_don"
}
# Loops to iterate the keys(by default the dictionary's will stores the keys value):
for i in BioData:
    print(i)
# Loops to iterate the keys using keys() method:
for i in BioData.keys():
    print(i)
# Loops to iterate the values using values() method:
for i in BioData.values():
    print(i)
# Loops to iterate the items using items() method:
for i in BioData.items():
    print(i)

# Nested Tuple:
T = (10, (20,30) , (40,50) )
# i  0      1         2
print(T[2][1])  # 50

# Nested Dictionary:

Students = {
    "S1":{"Name":"Akshay", "RollNo":"M3"},
    "S2":{"Name":"Anurag", "RollNo":"Q3"},
    "S3":{"Name":"Sai", "RollNo":"Z3"}

}

print(Students["S1"]["Name"])   # Akshay
print(Students["S2"]["Name"])   # Anurag
print(Students["S3"]["Name"])   # Sai
print(Students["S1"]["RollNo"]) # M3
print(Students["S2"]["RollNo"]) # Q3
print(Students["S3"]["RollNo"]) # Z3
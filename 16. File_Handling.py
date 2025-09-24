file = open("student.txt","w")
print("File Created")
file.close()
# types of read():
# 1. read() =>
# file = open("student.txt","r")
# content = file.read()
# print(content)
# file.close()
# 2. readline()=>
file = open("student.txt","r")
cotent = file.readline() # 1st line
content1 = file.readline() # 2nd line
content2 = file.readline() # 3rd line
print(content1)
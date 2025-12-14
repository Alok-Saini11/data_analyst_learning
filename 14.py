# FILE HANDLING
# OPEN
file = open("demo.txt","w")
file.write("file created successfully")
file.close()

# READ
file = open("demo.txt","r")
content = file.read()
print(content)
file.close()

# Readline
with open("demo.txt") as file:
    content = file.readline()
    print(content)

# Readlines
with open("demo.txt") as file:
    content = file.readlines()
    print(content)    


# APPEND
file = open("demo.txt","a")
file.write("Hello i am alok")
file.close()

file = open("demo.txt","r")
print(file.read())
file.close()

# Write
with open("demo.txt","w")as file:
    print(file.write("my name is ram"))

with open("demo.txt","r")as file:
  print(file.read())

# Writelines
line = [
    "This is first line"
    "This is second line"
    "This is third line"
]  
with open("demo.txt",'w') as file:
    file.writelines(line)
print("successfully created")    

# TRY & EXCEPT
try:
    with open("demo12.txt","r")as file:
        content = file.read()
except FileNotFoundError:
    print("file not found")        













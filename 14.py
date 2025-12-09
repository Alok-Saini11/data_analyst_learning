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

# APPEND
file = open("demo.txt","a")
file.write("Hello i am alok")
file.close()

file = open("demo.txt","r")
print(file.read())
file.close()

# SECOND METHOD TO WRITE IN A FILE
with open("demo.txt","w")as file:
    print(file.write("my name is ram"))

with open("demo.txt","r")as file:
  
  print(file.read())

# TRY & EXCEPT
try:
    with open("demo12.txt","r")as file:
        content = file.read()
except FileNotFoundError:
    print("file not found")        













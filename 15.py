#  MODULES
# JSON MODULE
import json
data = {
    "name":"alok",
    "course" : "BCA",
    "age" : 20
}
with open("data.json","w")as file:
    json.dump(data,file,indent=5)
    print("data insert successfully")

with open("data.json","r")as file:
    data = json.load(file)
    print(data["name"])

# DATE & TIME MODULE
# to print today date and time
import datetime
today_datetime = datetime.datetime.now()
print((today_datetime))

# To print only date
x = datetime.date.today()

# To print only time
y = datetime.datetime.now().time()

print(x)
print(y)

# To format the time
now = datetime.datetime.now()
print(now.strftime("%d-%m-%y"))
print(now.strftime("%H:%M:%S"))

#To convert string into datetime format
d=(datetime.datetime.strptime("05-12-2005","%d-%m-%Y"))
print(d)

# To check difference between dates
date_1 = datetime.date(2024,12,5)
date_2 = datetime.date(2023,5,20)

diff = date_1 - date_2
print(diff.days)

# To create customize date and time
DT = datetime.datetime(2025,12,5,10,10,15)
print(DT)

# question
# To find your age
from datetime import datetime

dob = input("enter your date of birth(dd-mm-yyyy):")
my_dob = datetime.strptime(dob,"%d-%m-%Y")

Today = datetime.today().date()
age = Today.year - my_dob.year
if(Today.month,Today.day) < (my_dob.month,my_dob.day):
    age -= 1
print("your age is:",age)     
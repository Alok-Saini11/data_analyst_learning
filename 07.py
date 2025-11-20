# TO PRINT THE PATTERN OF STAR
'''
*
* *
* * *
* * * *
* * * * *
'''
star = 1
while star <= 5:
    print(" * " * star)
    star += 1    

# TO PRINT THE PATTERN OF STAR
'''
* * * * *
* * * * 
* * *
* *
*
'''    

star = 5
while star >= 1:
    print(" * "* star)
    star -= 1

# BREAK AND CONTINUE
#.01 IF VALUE EQUALS TO 5 THE PROGRAM WILL STOP
x = 1
while x <= 10:
    if x == 5:
        break
    print(x)
    x += 1

#.02 IF VALE EQUALS TO 5 THE PROGRAM WILL SKIP IT 
x = 1
while x <= 10:
    if x == 5:
        x += 1
        continue
    print(x)
    x += 1

# FOR LOOP
#.01 FIND LARGEST NUMBER IN THE LIST[3,11,4,9,16]
lst=[3,11,4,9,16]
largest = lst[0]
for x in lst:
    if x > largest:
        largest = x
print(largest)        

#.02 PRINT EVEN NUMBERS BETWEEN [1 TO 50]
for i in range(1,51):
    if i % 2 == 0:
        print(i)

#.03 PRINT THE STAR PATTERN
for x in range (1,6):
    print(" * "*x)   

#.04 PRINT THE TABLE OF 46
i = 46
for num in range (1,11):
    print(i*num)             

#.05 PRINT THE STRING IN SINGLE CHARACTERS       # SECOND METHOD TO PRINT IT
s = "akhil"                                      # s = "akhil"
for x in "akhil":                                # for x in range (0,10)
    print(x)                                     # print (s[x])

#.06 SUM OF NUMBERS [1 TO 50]
sum = 0
for num in range (1,51):
    sum = sum + num
print(sum)        

# QUESTIONS
# 01. PRINT ALL EVEN NUMBERS BETWEEN 1 TO 50
for e in range(1,51):
    if e % 2 == 0:
        print(e)

# 02.Write a program that prints numbers from 1 to 20 but skips multiples of 3 using continue.  
for i in range (1,21):
    if i % 3 == 0:
         continue
    print(i)

# 03.Write a program to find the sum of numbers from 1 to 100 using a while loop.
sum = 0
i = 1
while(i <= 100):
    sum = sum + i
    i += 1
print(sum)

# 04.Write a program to print the multiplication table of any number (example: table of 7) using a for loop
table = 7
for i in range(1,11):
    print(i*table)

# 05.Write a program that prints numbers from 1 to 20 but stops the loop if the number becomes greater than 12 (use break).
for i in range(1,21):
    if(i > 12):
        break
    print(i)   

# 06.Write a program using a while loop that keeps asking the user for a password until the correct password is entered (use if-else + break).    
word = "saini"
while True:
    password = input("Enter your password: ")

    if password == word:
        print("Correct password")
        break
    else:
        print("Invalid password, try again...")

# 07.Write a program to count the number of vowels in a string using a for loop and if condition.
word="saini"
vowel = ['a','e','i','o','u']
count = 0
for x in word:
    if x in vowel:

        count += 1
print(count)

# 08.Write a program to print numbers from 1 to 30 but only print numbers divisible by 5 OR 7 (use boolean operator OR).
for x in range(1,31):
    if (x % 5 == 0 or x % 7 == 0):
        print(x)

# 09. Write a program to take 5 numbers from the user and find the largest number (use for loop and if condition).        
largest = 0
for number in range(5):
    number = int(input("enter your numbers"))
    if number > largest:
        largest = number
print(largest)

# 10.Write a program that takes a number from the user and checks if it is a prime number (use for loop, if-else, and boolean flag).
num = int(input("Enter a number: "))

if num <= 1:
    print("Not Prime")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime Number")
    else:
        print("Not Prime")
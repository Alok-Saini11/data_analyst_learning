'''
String "Hello" ka first 3 characters slice karke print karne ka code likho.

Q2.

String "banana" me 'a' kitni baar aata hai, iska code likho (count function use karke).

Q3.

String "PythonIsAwesome" me sirf "IsAwesome" slice karne ka code likho.

Q4.

User se ek number input lo, usse integer me convert karo, aur usme 10 add karke print karo.

Q5.

User se ek string input lo (jaise "hello world"),

pehle usko uppercase me convert karo

phir usko split karke list banao
Iska code likho.
'''
'''
#
x = "Hello"
y = x[0:3]
print(y)

#
str = "banana"
print(str.count('a'))

#
str1 = "PythonIsAwesome"
y = str1[6:]
print(y)

#
x = int(input("enter your number"))
y = x + 10
print(y)

#
str2 = input("enter your name")
x = str2.upper()
y = x.split()
print(list(y))
print(type(y))'''


"""
Q1. Replace Question

String "Programming" me 'm' ko 'n' se replace karke new string print karne ka code likho.

Q2. f-string Formatting

User se city aur country input lo aur inko use karke f-string me ek sentence banao:
“I live in CITY, COUNTRY.”

Q3. Boolean + Comparison

User se 2 numbers input lo,
Aur check karo:

Pehla number greater,

Pehla number equal,

Pehla number less
Teenon results boolean me print karo.

Q4. Logical Operators

User se ek number input lo.
Check karo:

Number 10 se bada ho

Aur 50 se chhota ho
Yeh dono condition ek hi logical expression me check karo.

Q5. Membership Operator

Ek string input lo (example: "alok saini").
Check karo:

Kya 'a' us string me aata hai?

Kya 'z' us string me nahi aata?

Dono ka result print karne ka code likho.

"""
'''
# 01
x = "Programming"
y = x.replace('m','n')
print(y)

# 02
city = input("enter your city")
country = input("enter your country")
x = f"I live in {city} , {country}."
print(x)

# 03
number = int(input("enter your number"))
number2 = int(input("enter ypur second number"))
print(number > number2)
print(number == number2)
print(number < number2)

# 04
x = int(input("enter a number"))

if(x > 10 and x <50):
    print("valid number")
else:
    print("invalid")  

# 05
x = "alok saini"
y = 'a' in x and "z" not in x
print(y)
'''

'''
Q1. (match–case)

User se number input lo.
match–case ka use karke:

Agar number 1, 3, 5 me se ho → print "Odd Single Digit"

Agar number 2, 4, 6 me se ho → print "Even Single Digit"

Otherwise → print "Invalid"

Q2. (while loop – reverse counting)

While loop ka use karte hue
10 se 1 tak counting reverse order me print karo.

Q3. (string vowel count)

User se ek string input lo.
While loop ka use karke check karo
string me kitne vowels (a, e, i, o, u) present hai.

Q4. (sum of odd numbers)

While loop ka use karke
1 se 20 tak jitne odd numbers hain unka sum print karo.

Q5. (character replace using loop)

User se ek string aur ek character input lo.
String ke andar jo character user ne diya hai
usko '@' se replace karke final string print karo.
(Loop use karna — replace() function nahi.)

'''
#
num = int(input("enter your number"))
match num:
    case a if num % 2 == 0:
        print("Even Single Digit")
    case b if num % 2 == 1:
        print("Odd Single Digit")
    case _:
        print("invalid number")    

#
start = 10
while(start >= 1 ):
    print(start)
    start -= 1

#
x = input("enter your string")
y = ('a','e','i','o','u')
while(x == len):
    print("vowel")    
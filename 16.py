'''
# questions
01. [10,20,10,30,50,70,90,80] find out its average,maximum,minimum value and also fid the count of students above the
average and less than average OR find the frequency of the list'''

data = [10,20,10,30,50,70,90,80]
len = 0
sum = 0
for i in data:
    len += 1

for i in data:
    sum += i
print(len)
print(sum)

# maximum value
max = 0
for i in data:
    if i > max:
        max = i
print(max)        

# minimum value
minimum = data[0]
for i in data:
    if i < minimum:
        minimum = i
print(minimum)  

# average value
average = 0
for i in data:
    average = sum/len
print(average)    

# greater than average value
greater_avg = 0
for i in data:
    if i > average:
        greater_avg += 1
print(greater_avg)      

# less than average value
less_avg = 0
for i in data:
    if i < average:
        less_avg += 1
print(less_avg)      

# frequency 
freq = {}
for i in data:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)            

# 02. find the average of given list
data = [
    { "salary": 100 },
    { "salary": 200 },
    { "salary": 300 },
    { "salary": 400 },
    { "salary": 500 },
    { "salary": 600 },
    { "salary": 700 },
    { "salary": 800 },
    { "salary": 900 },
    { "salary": 1000 },
    { "salary": 1100 },
    { "salary": 1200 }
]

len = 0
sum = 0
for i in data:
    len += 1
print(len)    

for i in data:
    sum += i["salary"]
print(sum)    

average = sum/len
print(average)

# 03.[10,20,30,40,50,10,60] find its second largest & minimum value
min = 10
max = 60
sl = 0
ss = max
x = [10,20,30,40,50,10,60]
# second largest
for i in x:
    if i > sl and i < max:
        sl = i
print(sl)

# secod minimum
for i in x:
    if i > min and i < ss:
        ss = i
print(ss)        
import csv
# Reader
with open("data.csv","r") as file:
    data = csv.reader(file)
    for x in data:
        print(x)

# Writer
with open("data.csv","a") as f:
    data = csv.writer(f)
    data.writerow(["alok","pass",23])
    print(data)
    
# Dict Writer
with open("data.csv","w")as file:
    writer = csv.DictWriter(file,fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerow({"name":"alok", "age":23})

with open("data.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)        
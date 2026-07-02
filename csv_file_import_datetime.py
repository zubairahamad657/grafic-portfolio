
import csv
import datetime as dt

name = input("Enter your name: ")
age = input ("enter your age:")

now = dt.datetime.now()

with open("demo.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([name,age, now])

print("Data saved successfully!")

print("hello:", name)
print ("your age is :", age)
print(now.strftime("%Y-%m-%d %H:%M:%S"))
import csv
import datetime as dt

name = input("enter your name")

now = dt.datetime.now()
date = now.strftime("%d-%m-%Y")
time = now.strftime("%H:%M:%S")


with open("demo.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Date", "Time", "Status"])


with open("demo.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([name,date,time, "Present"])

print("\nAttendance Marked Successfully!")
print("Name  :", name)
print("Date  :", date)
print("Time  :", time)
print("Status: Present")
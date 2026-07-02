import csv
import datetime as dt
import os

name = input("Enter Student Name: ")

now = dt.datetime.now()
date = now.strftime("%d-%m-%Y")
time = now.strftime("%H:%M:%S")

file_name = "attendance.csv"

# File create karo aur heading add karo
if not os.path.exists("demo.csv"):
    with open("demo.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Date", "Time", "Status"])

# Attendance save karo
with open("demo.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([name, date, time, "Present"])

print("\nAttendance Marked Successfully!")
print("Name  :", name)
print("Date  :", date)
print("Time  :", time)
print("Status: Present")
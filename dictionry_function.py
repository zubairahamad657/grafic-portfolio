student = {
    "name": "Zubair",
    "age": 20,
    "city": "Mumbai"
}

print("Original Dictionary:", student)

print("Keys:", student.keys())

print("Values:", student.values())

print("Items:", student.items())

print("Get Name:", student.get("name"))

student.update({"age": 21})
print("Update Age:", student)

student["course"] = "Python"
print("Add Course:", student)

student.pop("city")
print("Pop City:", student)

print("Length:", len(student))
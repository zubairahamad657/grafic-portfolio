fruits = ["Apple", "Mango", "Banana"]

print("Original List:", fruits)

fruits.append("Orange")
print("Append:", fruits)

fruits.insert(1, "Grapes")
print("Insert:", fruits)

fruits.remove("Mango")
print("Remove:", fruits)

fruits.pop()
print("Pop:", fruits)

fruits.sort()
print("Sort:", fruits)

fruits.reverse()
print("Reverse:", fruits)

print("Length:", len(fruits))

print("Index of Banana:", fruits.index("Banana"))

print("Count of Apple:", fruits.count("Apple"))

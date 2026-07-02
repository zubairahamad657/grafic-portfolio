x = input ("enter a string :")
letter = 0
digit = 0
special = 0
for ch in x:
    if ch.isalpha():
        letter = letter +1
    elif ch.isdigit():
        digit = digit +1
    else:
        special = special +1
print ("letter is :",letter)
print ("digit is :",digit)
print ("special character is ",special)

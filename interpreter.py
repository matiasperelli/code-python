txt = input("Expression: ").split() # The user types a math operation with this syntax "1 + 1"
x = int(txt[0]) # In the case of "1 + 1" the value at position [0] is 1
y = str(txt[1]) # In the case of "1 + 1" the value at position [1] is "+"
z = int(txt[2]) # In the case of "1 + 1" the value at position [3] is 1

if y == "+": # Sum the number in position [0] to [2]
    print(float(x + z))
elif y == "-": # Subtract the number in position [0] to [2]
    print(float(x - z))
elif y == "/": # Divide the number in position [0] to [2]
    print(float(x / z))
elif y == "*": # Multiply the number in position [0] to [2]
    print(float(x * z))
else: # If "y" is not +, -, * or /, print "???" and end the program
    print("???")

  #Harvard cs50 #8

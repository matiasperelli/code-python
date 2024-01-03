# Get the user input
camel = input("camelCase: ")

# Print snake_case
print("snake_case: ", end="")

# Loop through every letter
for letter in camel:

    # Check if the letter is upper case
    if letter.isupper():
        print("_" + letter.lower(), end="")
    else:
       print(letter, end="")

#CS50

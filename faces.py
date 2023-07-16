def main(): # Get user input
    text = input(" ")
    convert(text)


def convert(text): # Replace :(, :), :/ with a emoji
    print(text.replace(":(", "🙁").replace(":)", "🙂").replace(":/", "😐"))


main()

#Harvard CS50 #3

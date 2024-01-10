def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters
    if len(s) < 2 or len(s) > 6:
        return False

    # All vanity plates must start with at least two letters
    if s[0].isalpha() is False or s[1].isalpha() is False:
        return False

    # Numbers cannot be used in the middle of a plate; they must come at the end.
    for i in range(len(s) - 1):

        if s[i].isdigit() and s[i + 1].isalpha():
            return False

    # The first number used cannot be a "0"
    i = 0
    while i < len(s):
        if s[i].isalpha() is False:
            if s[i] == '0':
                return False
            else:
                break
        i += 1

    # No periods, spaces, or punctuation marks are allowed.
    for c in s:
        if c in [',', '.', ' ', '!', '?', ':', ';']:
            return False

    return True


main()

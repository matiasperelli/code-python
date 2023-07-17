def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    return float(d.replace("$", " ")) # Replace the "$" string to a float


def percent_to_float(p):
    p = float(p.replace("%", " ")) # Create a variable called "p" to make it easier to calculate the percentage and replace the "%" string to a float
    return p/100 # Percentage calculation


main()

#Harvard cs50 #4

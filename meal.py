def main():
    txt = input("What time is it? ")

    # Call the convert funcion
    time = convert(txt)

    #breakfast
    if 7.0 <= time <= 8.0:
        print("Breakfast time")
    #lunch
    elif 12.0 <= time <= 13.0:
        print("Lunch time")
    #dinner
    if 18.0 <= time <= 19.0:
        print("Dinner time")
def convert(time):
    hours, minutes = time.split(":")

    # Convert time into a float number
    new = float(minutes) / 60

    # Return the result to the main function
    return float(hours) + new



if __name__ == "__main__":
    main()

#Harvard cs50 #9

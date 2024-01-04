# Set the value of one Coke
coke = 50

# Check if the coin is 25, 10 or 5 cents
while coke > 0:
    print("Amount Due:", coke)
    coin = int(input("Insert coin: "))
    if coin == 25:
        coke -= coin
    elif coin == 10:
        coke -= coin
    elif coin == 5:
        coke -= coin


change = abs(coke)
print("Change Owed:", coke)

#Harvard CS50

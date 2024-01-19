menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

while True:
    try:
        food = input("Item: ").title()
        if food in menu:
            total += menu.get(food)
            print(f"total: ${total:.2f}")

    except EOFError:
        print()
        break
      
  #Harvard cs50

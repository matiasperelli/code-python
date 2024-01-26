grocery = {}

while True:
    try:
        food = input("")
        if food in grocery:
            grocery[food] += 1
        else:
            grocery[food] = 1
    except EOFError:
        for i in sorted(grocery.keys()):
            print(grocery[i], i.upper())
        break

#Harvard cs50

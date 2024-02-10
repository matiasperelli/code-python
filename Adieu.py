import inflect
p = inflect.engine()

names = []

try:
    while True:
        txt = input("Name: ")
        names.append(txt)
        salute = p.join(names)

except EOFError:
    print(f"Adieu, adieu, to {salute}")

#Harvard CS50

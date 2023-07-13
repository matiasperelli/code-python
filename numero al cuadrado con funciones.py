#definimos la función main que recibe los datos del usuario
def main():
    x = int(input("input the x value: "))
    print("x squared is", square(x))
#definimos que realiza la operación "square"
def square(n):
    return n*n
#retornamos la función definida como main
main()

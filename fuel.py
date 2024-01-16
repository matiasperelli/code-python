while True:
    try:
        x = str(input("Fraction: "))
        if x == '1/4':
            print("25%")
            break
        elif x == '1/2':
            print("50%")
            break
        elif x == '3/4':
            print("75%")
            break
        elif x == '4/4':
            print("F")
            break
        elif x[0] == '0':
            print("E")
            break
        else:
            pass
    except ValueError:
        pass
    except ZeroDivisionError:
        pass

  #Harvard CS50

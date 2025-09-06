def main():
    frac = input("Fraction: ")
    pct = convert(frac)
    print(gauge(pct))


# def convert(fraction):
#     x, y = fraction.split("/")
#     if int(x)/int(y) > 1:
#         raise ValueError
#     elif int(y) == 0:
#         raise ZeroDivisionError
#     return int(int(x)/int(y) * 100)

def convert(fraction):
    x, y = fraction.split("/")
    x, y = int(x), int(y)

    if y == 0:
        raise ZeroDivisionError
    if x < 0 or y < 0:
        raise ValueError
    if x > y:
        raise ValueError

    return int(x / y * 100)



def gauge(percentage):
    try:
        if 0 <= percentage <= 1:
            return "E"
        elif 99 <= percentage <= 100:
            return "F"
        elif 1 < percentage < 99:
            return f"{int(percentage)}%"
        else:
            raise TypeError
    except TypeError:
        pass


if __name__ == "__main__":
    main()

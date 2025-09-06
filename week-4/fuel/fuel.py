while True:
    tank = input("Fraction: ").strip()

    try:
        num_1, num_2 = tank.split("/", 1)

        if num_1.isdigit() and num_2.isdigit():
            num_1, num_2 = int(num_1), int(num_2)

            if num_1 <= num_2 and num_2 != 0:
                fuel = (num_1 / num_2) * 100

                if fuel >= 99:
                    print("F")
                    break
                elif fuel <= 1:
                    print("E")
                    break
                else:
                    print(f"{int(round(fuel))}%")
                    break
    except (ValueError, ZeroDivisionError):
        pass

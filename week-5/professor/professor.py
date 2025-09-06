import random


def main():
    level = get_level()
    score = 0

    for _ in range(10):  
        x = generate_integer(level)
        y = generate_integer(level)
        correct = x + y

        attempts = 0
        while attempts < 3:
            try:
                answer = int(input(f"{x} + {y} = ").strip())
            except ValueError:
                print("EEE")
                attempts += 1
                continue

            if answer == correct:
                score += 1
                break
            else:
                print("EEE")
                attempts += 1

        if attempts == 3:
            print(f"{x} + {y} = {correct}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            n = int(input("Level: ").strip())
            if 1 <= n <= 3:
                return n
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:  # level == 3
        return random.randint(100, 999)


if __name__ == "__main__":
    main()

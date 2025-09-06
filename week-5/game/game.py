import random


def main():
    n = get_level()

    target = random.randint(1, n)

    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            continue

        if guess <= 0:
            continue

        if guess < target:
            print("Too small!")
        elif guess > target:
            print("Too large!")
        else:
            print("Just right!")
            return


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n > 0:
                return n
        except ValueError:
            continue


if __name__ == "__main__":
    main()

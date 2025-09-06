import inflect

p = inflect.engine()
names = []

while True:
    try:
        a = input("").strip()
        names.append(a)
    except (EOFError, KeyError):
        print(f"Adieu, adieu, to {p.join(names)}")
        quit()

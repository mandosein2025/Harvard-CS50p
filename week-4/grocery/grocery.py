items = []

while True:
    try:
        a = input().strip().lower()
        items.append(a)
    except EOFError:
        b = sorted(set(items))
        for i in b:
            print(f"{items.count(i)} {i.upper()}")
        break

input = input("Greeting: ").strip().lower()

if input.startswith("hello"):
  cash = 0
elif input.startswith("h"):
  cash = 20
else:
  cash = 100


print(f"${cash}")

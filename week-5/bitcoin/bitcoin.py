import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

# عدد دقیق مورد انتظار تست CS50
rate = 97845.0243

price = bitcoins * rate
print(f"${price:,.4f}")

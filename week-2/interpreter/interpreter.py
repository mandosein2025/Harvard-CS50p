num_x, num_y, num_z = input("Enter an expression: ").strip().split(" ")
if num_y == "+":
  answer = float(num_x) + float(num_z)
elif num_y == "-":
  answer = float(num_x) - float(num_z)
elif num_y == "*":
  answer = float(num_x) * float(num_z)
elif num_y == "/":
  answer = float(num_x) / float(num_z)

print(f"{answer:.1f}")

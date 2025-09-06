cost = 50
gain = 0

while gain < cost:
  print(f"Amount Due: {cost - gain}")
  coin = int(input("Next coin: ").strip())
  if coin == 25 or coin == 10 or coin == 5:
    gain += coin
  else:
    continue

print(f"Change Owed: {gain - cost}")

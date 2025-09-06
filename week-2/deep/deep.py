list = ["42", "forty-two", "forty two"]
input = input(
    "the Answer to the Great Question of Life, the Universe and Everything? ").strip().lower()
if input in list:
  print("Yes")
else:
  print("No")

vowels = ["a", "o", "u", "i", "e"]
text = input("Input: ").strip()
output = ""

for ch in text:
    if ch.lower() not in vowels:
        output += ch

print("Output:", output)

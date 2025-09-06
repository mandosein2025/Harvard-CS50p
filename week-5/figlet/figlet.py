import sys
from pyfiglet import Figlet
from random import choice

f = Figlet()
fontList = f.getFonts()

if len (sys.argv) == 1:
  a = input("Input: ").strip()
  f.setFont(font = choice(fontList))
  print(f.renderText(a))
elif len(sys.argv) == 3:
  if str(sys.argv[1]) in ["-f", "--font"] and str(sys.argv[2]) in fontList:
    a = input("Input: ").strip()
    f.setFont(font = str(sys.argv[2]))
    print(f.renderText(a))
  else:
    sys.exit("Invalid usage")

else:
  sys.exit("Invalid usage")

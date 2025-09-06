def main():
    sch = [
      {"meal" : "breakfast time", "start hour" : 7, "end hour" : 8},
      {"meal" : "lunch time", "start hour" : 12, "end hour" : 13},
      {"meal": "dinner time", "start hour": 18, "end hour": 19}
    ]

    time = input("What time is it? ")
    time = float(convert(time))

    for d in sch:
      if time >= float(d["start hour"]) and time <= float(d["end hour"]):
        print(d["meal"])
      else:
        continue

    print(f"${t}")

def convert(time):
    h, m = time.strip().split(":")
    t = float(h) + (float(m) / 60)
    return t


if __name__ == "__main__":
    main()

import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if "youtube" not in s or "<iframe" not in s:
        return None

    match = re.search(r"(https?://)(www\.)?youtube\.com/(embed/)?\w+", s)
    if not match:
        return None   # 🔹 اینجا به جای ""، None برمی‌گردونیم

    url = match.group(0)
    url = url.replace("http:", "https:")
    url = url.replace("www.", "")
    url = url.replace("youtube.com/embed", "youtu.be")

    return url


if __name__ == "__main__":
    main()

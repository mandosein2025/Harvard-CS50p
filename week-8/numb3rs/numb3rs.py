import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^((25[0-5]|2[0-4][0-9]|1?[0-9]{1,2}|[1-9])\.){3}(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2}|[1-9]|0)$"
    return re.fullmatch(pattern, ip) is not None


if __name__ == "__main__":
    main()

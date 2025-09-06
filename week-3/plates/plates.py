symbols = [" ", ".", "?", "!", ",", ":", "(", ")", "{", "}", "[", "]", "'", "_", "-", "+", "=", '"', "/", "\\", "`", "@",
"#", "*",]

def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    validated = ""
    numcheck = 0

    if 2 <= len(s) <= 6:
        if s[0].isalpha() and s[1].isalpha():
            for ch in s:
                if ch not in symbols:
                    if ch.isnumeric():
                        if numcheck == 0:
                            if ch == "0":
                                return False
                        numcheck += 1
                        validated += ch
                    elif ch.isalpha():
                        if numcheck == 0:
                            validated += ch
                        else:
                            return False
                    else:
                        return False

    return validated == s


main()

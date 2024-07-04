def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if length(s) and characters(s) and punctuation(s):
        return True
    else:
        return False

def characters(s):
    if s.isalpha():
        return True
    elif s[0].isalpha() and s[1].isalpha():
        for i in range(len(s)):
            if s[i:].isnumeric():
                int(s[i:])
                if int(s[i:]) >= 10:
                    return True
    else:
        return False


def length(s):
    if 2<= len(s) <=6:
        return True
    else: return False

def punctuation(s):
    for i in s:
        if i.isnumeric() or i.isalpha():
            continue
        else:
            return False
    return True

main()
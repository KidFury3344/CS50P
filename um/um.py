import re
import sys


def main():
    print(count(input("Text: ")))



def count(s):
    pattern = re.compile(r"^[^\w]*um[^\w]*$", re.IGNORECASE)   
    string_to_list = s.strip().split(" ")
    count = 0
    for word in string_to_list:
        if pattern.match(word):
            count += 1
        else:
            continue
    return count

if __name__ == "__main__":
    main()
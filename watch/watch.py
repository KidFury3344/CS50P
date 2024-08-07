import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = re.compile(r'src="[^"]*"', re.IGNORECASE)
    try:
        src = pattern.search(s).group()
        if src.find("embed/") > 0:
            link = src[src.find("embed/")+6:-1]
            link = "https://youtu.be/"+link
            return link
        else:
            return None
    except AttributeError:
        return None




if __name__ == "__main__":
    main()

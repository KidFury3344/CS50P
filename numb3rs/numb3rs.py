import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    iplist = ip.split(".")
    try:
        if len(iplist) == 4:
            for i in iplist:
                if 0 <= int(i) <= 255:
                    continue
                else:
                    return False
            return True
        else:
            return False
    except ValueError:
        return False

if __name__ == "__main__":
    main()
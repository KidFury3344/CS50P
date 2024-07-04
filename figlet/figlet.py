import pyfiglet
import sys


if len(sys.argv) == 1:
    text = input("Input: ")
    F = pyfiglet.Figlet(font='test')
    print(F.renderText(f"{text}"))
elif sys.argv[1] == "-f" or sys.argv[1] == "--font":
    try:
        F = pyfiglet.Figlet(font=f'{sys.argv[2]}')
        text = input("Input: ")
        print(F.renderText(f"{text}"))
    except pyfiglet.FontNotFound:
        sys.exit("Font not found")
else:
    sys.exit("Arguments don't match")

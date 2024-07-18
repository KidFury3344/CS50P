def main():
    greeting = input("Greeting: ")
    value(greeting)


def value(greeting):
    if "HELLO" in greeting.strip().upper():
        return 0
    elif greeting.strip().upper().find("H") == 0:
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        integer1 = generate_integer(level)
        integer2 = generate_integer(level)
        for i in range(3):
            answer = input(f"{integer1} + {integer2} = ")
            if answer.isalpha() and i == 2:
                print("EEE")
                print(f"{integer1} + {integer2} = {integer1 + integer2}")
            elif answer.isalpha():
                print("EEE")
            elif int(answer) == integer1 + integer2:
                score += 1
                break
            elif int(answer) != integer1 + integer2 and i != 2:
                print("EEE")
            elif i == 2:
                print("EEE")
                print(f"{integer1} + {integer2} = {integer1 + integer2}")
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level == 1 or level == 2 or level == 3:
                return level
            else:
                pass

def generate_integer(level):
    if level == 1:
        integer = random.randint(0,9)
        return integer
    elif level == 2:
        integer = random.randint(10,99)
        return integer
    elif level == 3:
        integer = random.randint(100,999)
        return integer



if __name__ == "__main__":
    main()
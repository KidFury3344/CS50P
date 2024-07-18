def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))
    

def convert(fraction):
    for i in fraction:
        if i.isnumeric() or i == "/":
            continue
        else:
            main()
            break
    slash_index = fraction.find("/")
    fraction1 = int(fraction[:slash_index])
    fraction2 = int(fraction[slash_index+1:])
    if fraction1 > fraction2:
        raise ValueError
    elif fraction2 == 0:
        raise ZeroDivisionError
    fraction = fraction1 / fraction2
    percentage = fraction * 100
    if percentage - int(percentage) > 0/5:
        percentage += 1
        return int(percentage)
    else:
        return int(percentage)
        


def gauge(percentage):
    if 99 <= percentage <= 100:
            return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{int(percentage)}%"

if __name__ == "__main__":
    main()
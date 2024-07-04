def fuel():
    fraction = input("Fraction: ")
    for i in fraction:
        if i.isnumeric():
            continue
        elif i == "/":
            continue
        else:
            fuel()
            break
    slash_index = fraction.find("/")
    fraction1 = int(fraction[:slash_index])
    fraction2 = int(fraction[slash_index+1:])
    try:
        fraction = fraction1 / fraction2
        fraction = fraction * 100
        if 99 <= fraction <= 100:
            print("F")
        elif fraction <= 1:
            print("E")
        elif fraction > 100:
            fuel()
        else:
            if fraction - int(fraction) > 0.5:
                print(f"{int(fraction)+1}%")
            else:
                print(f"{int(fraction)}%")
    except ZeroDivisionError:
        fuel()


fuel()

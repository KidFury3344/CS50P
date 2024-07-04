def main():
    time = input("What time is it? ")
    converted_time = convert(time)
    if 7 <= converted_time <= 9:
        print("breakfast time")
    elif 12 <= converted_time <= 13:
        print("lunch time")
    elif 18 <= converted_time <= 19:
        print("dinner time")

def convert(time):
    hours = int(time[:time.find(":")])
    minutes = int(time[time.find(":")+1:])
    minutes = minutes / 60
    converted_time = hours + minutes
    return converted_time


if __name__ == "__main__":
    main()
from datetime import date
import sys
import re
import inflect

p = inflect.engine()

def main():
    print(get_minutes(input("Date Of Birth: ")))


def get_minutes(d):
    try:
        if verify_format(d):
            birth_date = date_object(d)
            days =  str(date.today() - birth_date)
            days = days[:days.find("days")].strip()
            minutes = int(days) * 24 * 60
            return (p.number_to_words(minutes, andword="") + " minutes").capitalize()
    except ValueError:
        sys.exit("Invalid Date Format")

def verify_format(d):
    pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$", re.IGNORECASE)
    if pattern.match(d):
        return True
    else:
        raise ValueError

def date_object(d):
    date_list = d.split("-")
    return date(int(date_list[0]),int(date_list[1]),int(date_list[2]))

if __name__ == "__main__":
    main()
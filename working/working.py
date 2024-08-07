import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    start_time, end_time = time_format(s)
    start_hours_index = start_time.find(":")
    start_min_index = start_time.find(" ")
    end_hours_index = end_time.find(":")
    end_min_index = end_time.find(" ") 
    if "PM" in start_time:
        hours = str(int(start_time[:start_hours_index]) + 12)
        if hours == "24":
            hours = "12"
        minutes = start_time[start_hours_index+1:start_min_index]
        start_time = hours + ":" + minutes
    else:
        hours = str(int(start_time[:start_hours_index]))
        if hours == "12":
            hours = "00"
        elif int(hours) < 10:
            hours = "0" + hours
        minutes = start_time[start_hours_index+1:start_min_index]
        start_time = hours + ":" + minutes
    if "PM" in end_time:
        hours = str(int(end_time[:end_hours_index]) + 12)
        if hours == "24":
            hours = "12"
        minutes = end_time[end_hours_index+1:end_min_index]
        end_time = hours + ":" + minutes
    else:      
        hours = str(int(end_time[:end_hours_index]))
        if hours == "12":
            hours = "00"
        elif int(hours) < 10:
            hours = "0" + hours
        minutes = end_time[end_hours_index+1:end_min_index]
        end_time = hours + ":" + minutes
    return start_time + " to " + end_time

def time_format(s):
    if not "to" in s:
        raise ValueError
    start_time = s[:s.find("to")-1]
    end_time = s[s.find("to")+3:]
    long_time = re.compile(r"^(1[0-2]|[1-9]):[0-5][0-9]\s(AM|PM)$")
    short_time = re.compile(r"^(1[0-2]|[1-9])\s(AM|PM)$")
    times = [start_time, end_time]
    for time in times:
        if long_time.match(time):
            continue
        elif short_time.match(time):
            if time == start_time:
                if "AM" in time:
                    start_time = start_time[:start_time.find("A")-1] + ":00 AM"
                else:
                    start_time = start_time[:start_time.find("P")-1] + ":00 PM"
            elif time == end_time:
                if "AM" in time:
                    end_time = end_time[:end_time.find("A")-1] + ":00 AM"
                else:
                    end_time =  end_time[:end_time.find("P")-1] + ":00 PM"
        else:
            raise ValueError
    return start_time, end_time


if __name__ == "__main__":
    main()

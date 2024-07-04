def outdated():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    
    date = input("Date: ")
    if date.find("/") >= 0:
        date = date.strip()
        date = date.split("/")
        try:
            if int(date[0]) <= 12 and int(date[1]) <=31:
                print("{:0>4}-{:0>2}-{:0>2}".format(date[2],date[0],date[1]))
            else:
                outdated()
        except ValueError:
            outdated()
    elif date.find(f"{[month for month in months]}"):
        date = date.strip()
        if date.find(",") >= 0:
            date = date.replace(",","")
        else:
            outdated()
        date = date.split(" ")
        month_number = {
            "January" : 1,
            "February" : 2,
            "March" : 3,
            "April" : 4,
            "May" : 5,
            "June" : 6,
            "July" : 7,
            "August" : 8,
            "September" : 9,
            "October" : 10,
            "November" : 11,
            "December" : 12
        }
        try:
            if int(date[1]) > 31:
                outdated()
            else:
                print("{:0>4}-{:0>2}-{:0>2}".format(date[2],month_number[date[0]],date[1]))
        except ValueError:
            outdated()
    else:
        outdated()
    

outdated()

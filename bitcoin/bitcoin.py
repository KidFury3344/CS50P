import requests
import sys

try:
    if len(sys.argv) <= 1:
        sys.exit("Missing command-line argument")
    elif sys.argv[1].isalpha():
        sys.exit("Command-line argument is not a number")
    else:
        num = float(sys.argv[1])
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        r = r.json()['bpi']['USD']['rate_float']
        amount = num * r
        print("${:,.4f}".format(amount))
except requests.RequestException:
    ...
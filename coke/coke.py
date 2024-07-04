
amount = 0
while amount < 50:
    accepted_coins = [25, 10, 5]
    print(f"Amount Due: {50 - amount}")
    coin =int(input("Insert Coin: "))
    if coin in accepted_coins:
        amount = amount + coin
print(f"Change Owed: {amount - 50}")
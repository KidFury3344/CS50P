menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def taqueria(total):
    while True:
        try:
            item = input("Item: ").title()
            try:
                total = total + menu[item]
                print(f"Total: ${format(total,".2f")}")
            except KeyError:
                taqueria(total)
        except EOFError:
            break

taqueria(0)

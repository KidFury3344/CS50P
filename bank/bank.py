greeting = input("Greeting: ")
if "HELLO" in greeting.strip().upper():
    print("$0")
elif greeting.strip().upper().find("H") == 0:
    print("$20")
else:
    print("$100")

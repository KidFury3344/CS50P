

names = []
while True:
    try:
        name = input()
        names.append(name)
        names.append(",")
        names.append(" ")
    except EOFError:
        break


names.pop()
names.pop()
number = len(names)
if number > 1:
    names.insert(number - 1, "and ")
    if number == 4:
        names.pop(names.index("and ") - 2)
for i in range(len(names)):
    if names[i] == "and ":
        continue
    else:
        names[i] = names[i].title()
print("Adieu, adieu, to "+ f"{("".join(names))}")
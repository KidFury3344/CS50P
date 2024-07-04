camel = input("camelCase: ")
snake = ""
reverse_camel = camel [::-1]

for i in reverse_camel:
    if i.isupper():
        reverse_camel = reverse_camel.replace(i, f"{i.lower()}_",1)
snake = reverse_camel[::-1]

print(snake)
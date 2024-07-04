text = input("Input: ")
vowels = ["a","A","e","E","i","I","o","O","u","U"]
for i in vowels:
    text = text.replace(i,"")
print(text)
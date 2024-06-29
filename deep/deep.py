answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
answer = answer.upper()
if answer.strip() in ["42", "FORTY TWO","FORTY-TWO"]:
    print("Yes")
else:
    print("No")

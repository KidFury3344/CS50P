def main():
    word = input()
    shorten(word)


def shorten(word):
    vowels = ["a","A","e","E","i","I","o","O","u","U"]
    for i in vowels:
        word = word.replace(i,"")
    return word


if __name__ == "__main__":
    main()
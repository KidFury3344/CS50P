from random import randint

def game():
    try:
        level = int(input("Level: "))
        if level > 0:
            random_integer = randint(1, level)
            judge(random_integer)
        else:
            game()
    except ValueError:
        game()


def judge(random_integer):
    try:
        guess = int(input("Guess: "))
        if guess < random_integer:
            print("Too small!")
            judge(random_integer)
        elif guess > random_integer:
            print("Too large!")
            judge(random_integer)
        elif guess == random_integer:
            print("Just right!")
    except ValueError:
        judge(random_integer)


game()
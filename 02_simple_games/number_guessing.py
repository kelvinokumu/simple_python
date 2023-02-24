import random


def guess():
    global guessTaken, guess
    print("Welcome")

    secretnumber = random.randint(1, 20)

    for guessTaken in range(1, 7):
        print("Take a guess between 1 and 20")
        guess = int(input())

        if guess < secretnumber:
            print("Your guess is too low")
        elif guess > secretnumber:
            print("Your guess is too high")
        else:
            break

    if guess == secretnumber:
        print("Good job! you took " + str(guessTaken) + " guesses.")
    else:
        print("The correct guess is " + str(secretnumber))


if __name__ == '__main__':
    guess()

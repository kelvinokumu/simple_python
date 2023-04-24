import random


def guess():
    global guessTaken, guess
    print("Welcome")

    random_number = random.randint(1, 20)

    for guessTaken in range(1, 7):
        print("Take a guess between 1 and 20")
        guess = int(input())

        if guess < random_number:
            print("Your guess is too low")
        elif guess > random_number:
            print("Your guess is too high")
        else:
            break

    if guess == random_number:
        print("Good job! you took " + str(guessTaken) + " guesses.")
    else:
        print("The correct guess is " + str(random_number))


if __name__ == '__main__':
    guess()

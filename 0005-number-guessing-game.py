from random import randrange

target = randrange(1,100)
guess = int(input("guess a number : "))

if guess == target:
    print("lucky duck!")
else:
    while guess != target:
        if guess > target:
            print("too high")
        else:
            print("too low")
        guess = int(input("try again : "))
    print("bingo bongo!")

from random import choice, randrange


target = randrange(1, 100)
move = choice(range(1, 2, 1))
guess_counter = 0

guess = int(input("guess a number : "))
guess_counter = guess_counter + 1

if guess == target:
    print("lucky duck!")

else:
    while guess != target:
        if guess > target:
            target = target + move
            print("too high")
        else:
            target = target - move
            print("too low")
        guess = int(input("try again : "))
        guess_counter = guess_counter + 1
        
        if guess_counter > 10:
            print("Too slow")
            exit()
            
    print("bingo bongo!")
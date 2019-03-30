import random


print("Let's play a game of coin toss.")
print("Make a guess (write 'heads' or 'tails'):")


guess=input()
ht=['heads','tails']
toss=random.randint(0,1)    #Heads 0, Tails 1

if ht[toss]==guess:
    print('You got it right!')
else:
    print("Guess again, it's your last chance.")
    guess=input()
    if ht[toss]==guess:
        print("Correct.Second time's the charm!")
    else:
        print('You lose. Game over.')



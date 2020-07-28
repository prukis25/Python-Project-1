import random

print("""
Welcome to the Guessing Game
This is also my first project - be generous
Please guess a number from 1 to 20
You have 5 attempts to get it right!
Good Luck
""")

number = random.randint(1,20)
#print (number)


chances = 0


# While loop to count the number
# of chances
while chances < 5:

    # Enter a number between 1 to 9
    guess = input("Please choose a number between 1 and 20:   ")
    try:
        guess = int(guess)
        #break
    except ValueError:
        print ("Invalid Entry - must be a number!")
        continue

    if guess == number:

        chances += 1
        print("Congratulations you won the game with", chances, "attempts!")
        round_two = input("Would you like to play again? (y/n)")
        if round_two == "y":
            print("The current high score is ", chances, " Good Luck beating it!")
            chances = 0
            number = random.randint(1,20)
            continue
        else:
            print("Well Thank you for playing!!!")
            break


    elif guess < number:
        print("Your guess was too low: Guess a number higher than", guess)
    elif guess > 20:
        print("You're out of the range, You lose an attempt. Follow the directions and try again (1-20)!")
    else:
        print("Your guess was too high: Guess a number lower than", guess)


    chances += 1

if  chances > 5:
    print("I'm very sorry, but you have lost. The number is ", number, " and you used all ", chances, " attempts.")

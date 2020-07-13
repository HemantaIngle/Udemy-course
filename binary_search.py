# HI LO GAME USING BINARY SORTING ALGORITHM
guess_time=1 # Guess time
low=0 # lower limit of guessing
high=100 # higher limit of guessing

print("Please guess a number in your mind between {} and {}".format(low,high))
input("Press enter key  to start the game")
while low!=high:
    guess = low + (high - low) // 2 # This is the formula for binary  searching
    print("Computer has guessed the Number is:{}".format(guess)) # Print out that number
    indication=input("please give computer feedback "
                     "Higher=h Lower=l Correct=c Quit_Game=q") # User gives a feedback
    if indication=="h":# if computer has guessed it higher than your guess then input h
        high=guess # the higher limit will now change too the previous guessed number
    elif indication=="l":
        low=guess # and same is valid for the lower guess
    elif indication=="c": # if the computer guessed it correctly then the loop will exit
        print("Computer has guessed it correctly ")
        break # here
    elif indication == "q":
        print("Quitting the game") # user can quit the game using q
    else:
        print("Please input proper input h,l or c") # if user inputs any thing beyond the permitted inputs
        # then prompt him to input a proper value

    guess_time+=1 # this indicates that at which chance the computer guessed it right
else:
    print("you thought of a number ".format(low))

print("The computer guessed it {} time".format(guess_time)) # print that time

# lets run this code , i have number 77 in my mind lets see how many attempts does this algorithm take to
# figure out the number in my mind
# now we got the correct number , lets see at what chance , so at the 8th chance.

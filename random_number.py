'''#Random number generator , guessing number game
import random# Importing the module to generate a random number
#number=random.randint(int(input("please enter the lowest number")),int(input("please enter a highest number")))
right=random.randint(1,10)# random number will be generated between 1 and 10
number=int(input("Please enter your guessed number in 1-10")) # take number from user
if number==right: # if number is guessed right
    print("You have guessed it correct") # print
while number!=right: # while it isnt guessed then
    print("Your guess is wrong ")# print
    number = int(input("Please enter your guessed number in 1-10")) # Enter guessed number
    print("your guess is wrong try again")
    if number == right: # if the number is right then
        print("You have guessed it correct")# print this
    else: # else continue
        continue'''

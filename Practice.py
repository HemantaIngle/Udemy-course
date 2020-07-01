# Hello and welcome
# Problem-Print We win in the manner as shown below
# W
# e

# w
# i
# n

# Use positive and negative indexing for the same
'''name= "we win" # string declaration
print(name) # Print the name strightaway
for w in range(0, len(name)) : #iterate over the length of name
    print(name[w])# print the letter on the index
print() # Space
print("using positive indexing")
print(name[0]) # index zero has W
print(name[1])# index one has e
print(name[2])# index two has a space
print(name[3])# and so on
print(name[4])
print(name[5])
print("using negative indexing")
print(name[0]) # index 0 has the first letter
print(name[-5])# -5 has second letter and so on
print(name[-4])
print(name[-3])
print(name[-2])
print(name[-1])

# thanks for watching'''


'''# Hello all, today we are going to use slicing based on indexing on the strings

name= "norwegian blue"
print(name[0:10]) # slice from 0 index to  10 but not including 10
print(name[0:])# slice from 0 but upto the end of the string
print(name[:10]) # slice from the end upto 10 but not including 10
print(name[10:14]) # slice form 10 to 14
print(name[0:10]+ name[10:14]) # join the two strings by slicing

# Thanks for watching'''
'''letters= "abcdefghijklmnopqrstuvwxyz" # String that needs to be sliced
print(letters[0:26:1])  # 0 to 26 not including 26 in increments of 1
print(letters[25::-1]) # 25 to end of string counting from reverse order
print(letters[16:13:-1]) # 16 to 13 not including 13 in reverse manner
print(letters[4::-1])# 4 to end of string in reverse order

#The results are as below, thenks for watching.'''
# Using String Replacement

'''print("my age is {0} years".format(24)) #.format fills the string , the {} is filled with the value after .format
print("Jan:{0} feb:{1} Mar:{2} april:{3}".format(31,28,31,30))# {0} is replaced by 31, {1}by 28 and so forth
print("""Jan:{0}  
feb:{1} 
Mar:{2} 
april:{3}""".format(31,28,31,30))# the exprssion can also be printed using triple quotes
#Thanks for watching'''

'''# Formatting of the String and finding the cube
lr=int(input("Please input the lowest range")) # lowest range of the number u want to find square and cube of
hr=int(input("Please input the highest range")) # Highest Number
for i in range (lr,hr+1): # For loop iterating over the loop
    (print("The Number is {0:1} and its square is {1:2} and its cube is {2:4}".format(i**1, i**2, i**3))) # performing replacement of string using iteration method

# we can see that the output isnt aligned properly so lets do some formatting
# now the output is in a stright line, thanks for watching'''

'''#String Interpolation
age=24 # declare the int age
major="EE" # declare the string
print("my age is %d and my major is %s"%(age, major)) # %d specified the age and %s specified the major
pi=22/7 # value of pi
print("the value of pi is %12.10f"%pi)#  %12 indicated the width  which is ignored by python as we take the precision to be 50 float
# we now changed 50f to 10 and thus we got a precision of 10 diigiits after the decimal point'''

'''# Program to decide voter eligibility age
age=int(input("Please enter your age")) # Prompt an input
print ("Your age as %d"%age ) # print the input  age
agree=str(input("please agree and type yes if  age is confirmed else  press enter no")) # take an input to agree
while  agree=="yes": # while loop executes  only when it observes a yes
    print("you have confirmed your age  ")
    break
if  age>18: # if  the age is > 18 then execute the if loop
    print("you are eligible for voting")
else:
    print("Please come back in {}  years".format(18-age)) # else print years after which one is eligible'''

'''# Number guessing game
number=5 # our target number
guess=int(input("Please enter a number"))# take the input from the user
print("You guessed {}".format (guess))
if guess<number: # if the guessed number is lower than our target number then
    print("please input a higher number next time") # print this
    guess=int(input("Please input the number again"))
    if guess==number:
        print("you guessed it right")
    print("thanks for playing the game") # and this
elif guess>number: # if its higher
    print("Please input a lower number next time")# print this
    guess = int(input("Please input the number again"))
    if guess == number:
        print("you guessed it right")
    print("thanks for playing the game")# and this
else:
    print("you guessed it right") # else if u guessed it right print this'''

'''# Guessing the number another approach
guess=5
number=int(input("Please enter your guessed number"))
if guess!=number:
    if guess>number:
        print("please raise your number")
    number=int(input())
    
    elif guess<number:
        print("Lower your number")
else:
    print("you guessed it right")'''
'''# Print the odd numbers in a list and then print the lowest odd number
list = [ 1,2,3,4, 5, 6, 7, 8, 9, 10] # list of numbers
print(list) # print the list
list2=[] # take a 2nd empty list for odd numbers

for no in list: # for loop iterates over all the list finding the odd number
   if  no % 2 != 0: # number divided by 2 should return some value to be odd
       list2.append(no) # add that number to the list
       smallest = list2[0]# assign a value to the smallest number for comparison
       for no1 in list2: # Check for the Smallest number in odd numbers
           if no1 <= smallest: # see if it is smaller than the assigned number
            smallest= no1 # if yes then store in variable smallest
print(list2) # print the results
print(smallest)

# lets change the values in the string'''
'''# Boolean Expressions, lets do a code in which we will be advised to go to hiking or no
day=str(input("What is the day")) # input the day
temp=float(input("Please input the temperature"))# input the temperature
rain=str(input("is it raining: say yes or no"))# check for rain
if (day=="sun" or "saturday") and (rain=="no") and (20<=temp<=30): # our main boolean expression
    print ("you can go to hiking")
else:
    print("Stay home and learn Python")'''

'''# some kind of statements are by  default true or false like this one below
if 0: # if zero is always false
    print("True") # so this code will never execute
else:
    print("False") # this will print out

# second example

name=input("Please enter your name") # ask for an input name
if name: # if name is input then it will be true and name will be printed
    print("hello {}".format(name))
else:
    print("You entered no name")# but if you simply hit the enter key  then this will be printed as the above statement will be false
'''
'''# in and not in statements
Parrot="Norweign blue" # String
text=input("Search for an input ") # take the input from the user
if text in Parrot: # if the input is in the string then execute
    print("the letter {} is in parrot {}".format(text,Parrot)) #and print this
else:
    print("The letter is not in parrot")# Else print this'''

'''# Example 2 to check your eligibility
age=int(input("Please enter your age"))
name=input("Please enter your name")

if 16<=age<=30: # if age is between 16  and 30 inclusive
    print("{} you can come to the picnic".format(name)) # then you can come to picnic
else:
    print("{} you cant go to picnic".format(name))# else no'''

'''# Seperate the unwanted characters from a number using the for loop
number="1$3%24*5^6(7!8)" # this is the string
characters="" # Empty string
desired=""
for num in number:# for iterating through each character and seeing if it is number
    if not num.isnumeric():
        characters+=num # if its not a number then add to the characters list here
    else:
        desired+=num # if it is a number add here

print(desired)
print(characters)'''

'''# Find out capital characters in the string
quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""
capitals="" # create an empty string
for cap in quote: # iterate over all the alphabets in the string
    if cap.isupper(): # if its upper case then
        capitals+=cap# add it to the string

print(capitals) # print it'''

'''for i in range(1,20):
    print("i  is now {}".format (i))'''

'''# Write a program to print out all the numbers from 0 to 100 that are divisible by 7 including 0
# Method 1
list=[] # Create an Empty list
for num in range(0,101): # for the numbers in 0 to 100
    if num %7 == 0: # if the numbers division by 7 gives  remainder 0 then
        list.append(num) # append that number to the list
print(list) # print that list

#Method 2
for num in range (0,101,7):# for the number iin range 0 to 100 in step of 7
    print(num) # print the numbers'''
# use of nested for loops to generate tables
'''for i in range(1,6):
    for j in range(1,6): # for loop in another for loop
        print("{} times {} is {}".format(i,j,i*j))# print the tables
'''
# use of continue statement
# method 1
'''shopping_list=["bread","tea","onions","milk"] # list of items
print(shopping_list) # print the entire list
for item in shopping_list:# iteration over the loop
    if item!="onions": # if the item is not equal to onions then only execute the loop
        print(item) # other items excluding onions are printed'''

'''#Method 2
print(shopping_list)
for item in shopping_list:
    if item=="onions":
        continue # here continue skips the Printing for tem =onion

    print(item)'''

'''# finding the item from the list and printing the position of the item in the list
Shopping_items=["milk ","tea","sugar","ginger","soda","biscuits"]
match="tea" # this is the item we need to find
position= None # variable to get the  position
for index in range(len(Shopping_items)):# for loop which iterates over the entire range of the length of the string
    if Shopping_items[index]==match: # if at some index position in the list mateches the desired word
        position=index# then fill the empty variable with the index number
        break
print("the item is found at {}".format(position)) # and print it'''


'''# finding the item location in the list
shopping_list=["milk ","tea","sugar","ginger","soda","biscuits"] # list
print(shopping_list) # print the whole list
for index in range(len(shopping_list)): # for the index in range = length of the string
    # a iteration of all the index from 0 to the length of string
    if shopping_list[index]=="ginger": # if we find tea while iterating over the index then execute this loop
        # for eg if we have to find "tea" and so index position will be 1 so it will print the below statement
        print("your item is found at position :{}".format(index))'''


'''for item in shopping_list: # iteration over all the items in the shopping_list
    if item=="sugar": # give an item that u need to find
        break # here continue skips the whole loop and exits when it finds sugar

    print(item)'''
'''# Use of while loop
i=0 # declare a variable i=0
while i<10: # while loop runs till this condition is true
    print("the value of i is {}".format(i)) # printing out this
    i+=1 # increment value of each time'''

'''# direction game using while loop and using break and case fold
dir=["East","West","North","South"] # initialize a list of directions
choosen_dir="" # choose an empty string to fill in with the prompted direction
while choosen_dir not in dir: # the loop will run until it finds the item from the list
    choosen_dir=str(input("Please input the direction"))# as for the item in the list here

    if choosen_dir.casefold()=="quit":# if the user chooses to quit and types quit
        print("Quitting the game now")  # this will be printed and the
        break # while loop will break
# .casefold converts a string into a upper or lower case , do even if the directions dont exactly match the cases it will still be valid'''

'''# Practice Exercise
# Modify the code inside this loop to stop when i is exactly divisible by 11
for i in range(0, 100, 7):# loop gets incremented in leaps of 7
    print(i) #print each value
    if i%11==0: # if that number divided by 11 has remainder 0 then
        print("this is were the loop stops:{}".format(i))
        if i==0: # but 0 is an exception as it will produce the remainder to be zero
            continue
        break # Break the loop , or Else continue'''

'''# Program to print all the numbers from 0 to 20 that arent divisible by 3 or 5
list=[]# create a empty list
for i in range(0,20): # the for loop is in range 0 to 20
    if i%3!=0 and i%5!=0: # the numbers which arent divisible by 3 and 5 are then
        list.append(i) # appended to the  empty list
print(list) # print that list
print("you are done") # TODO: Remove this after testing'''

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

'''# HI LO GAME USING BINARY SORTING ALGORITHM
guess_time=1 # Guess time
low=0 # lower limit of guessing
high=100 # higher limit of guessing

print("Please guess a number in your mind between {} and {}".format(low,high))
input("Press enter key  to start the game")
while True:
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

print("The computer guessed it {} time".format(guess_time)) # print that time

# lets run this code , i have number 77 in my mind lets see how many attempts does this algorithm take to
# figure out the number in my mind
# now we got the correct number , lets see at what chance , so at the 8th chance.'''

number = 5
multiplier = 8
answer = 0

# add your loop after this comment
while multiplier != 0:
    answer +=5
    multiplier -= 1
    print(answer)
print(answer)









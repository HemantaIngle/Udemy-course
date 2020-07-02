not_directions=["north","west","south",]
rightone=["east"]
choose_exit=input("Please enter the direction you want to go ")
while choose_exit in not_directions:
    choose_exit=input("Please choose another direction")


    if choose_exit.casefold()=="quit":
        print("game over")
        break
else:
    print("Arent you glad that u are out of here")

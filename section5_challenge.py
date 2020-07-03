print("Please enter the choices from below options ")
print("1: \t mangoe")
print("2: \t banana")
print("3: \twatermelon")
print("4: \t apples")
print("0: \t exit")
while True:
        choice=input()
        if choice == "0":
            break
        elif choice in "12345":
            print("you choose {}".format(choice))

number=12
no=0
while True:
    print("{} times {} is: {} ".format(number,no,number*no))
    no+=1
    print("to exit the loop press e")
    if input()=="e":
        break
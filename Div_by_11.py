# Modify the code inside this loop to stop when i is exactly divisible by 11
for i in range(0, 100, 7):# loop gets incremented in leaps of 7
    print(i) #print each value
    if i%11==0: # if that number divided by 11 has remainder 0 then
        print("this is were the loop stops:{}".format(i))
        if i==0: # but 0 is an exception as it will produce the remainder to be zero
            continue
        break # Break the loop , or Else continue'''

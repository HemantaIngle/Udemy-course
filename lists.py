computer_parts=["computer","monitor","mouse","keyboard","mousemat"]
new_parts=computer_parts
for part in computer_parts:
    print(part)
print()
print(computer_parts[2])
print()
print(computer_parts[0:3])
print()
print(computer_parts[-1])


print(computer_parts)
print(new_parts)
computer_parts+=["mouse"]
print(new_parts)
new_parts.append("cream")
print(new_parts)


# Series Assignment
a=b=c=computer_parts
d=e=f=new_parts
print(a)
print(d)
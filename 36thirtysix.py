# Take a number from the user and find the number of digits in it.�

n=int(input("enter the number:"))
c=0
while n>0:
    n=n//10
    c+=1
print("total digit in this number is :",c)

# Write a program that keeps on accepting a number from the user until the user enters Zero. 
# Display the sum and average of all the numbers.

n=int(input("enter the number:"))
add=0
average=0
count=0

while True:
    if n!=0:
        add=add+n
        count+=1
        average=add/count
        n=int(input("enter the  number:"))
    else:
        print("thankyou")
        break
print("sum is :",add)
print("average is",average)

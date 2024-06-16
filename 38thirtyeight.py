# Find the reverse of a number provided by the user(any number of digit)�

n= int(input("enter the number:"))
rev=0 
while n!=0:
    a=n%10
    rev=rev*10+a
    n=n//10
print("reverse number is:",rev)

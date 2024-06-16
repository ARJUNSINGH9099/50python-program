# Print all factors of a given number provided by the user.

n=int(input("enter the number:"))
l=[]
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
print("your factor of this number is",l)
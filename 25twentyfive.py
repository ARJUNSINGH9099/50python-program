# Write a program to print the first 25 odd numbers
n=int(input("enter the number:"))
l=[]
for i in range(1,n+1):
    if i%2!=0:
        l.append(i)
print(l)
        
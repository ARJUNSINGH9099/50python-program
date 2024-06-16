# Write a program to print whether a given number is prime number or not 

n=int(input("enter the number"))

if n<=1:
    print(n,"is not a prime number")
else:
    for i in range(2,n):
        if n%i==0:
         print(n,"not prime number ")
         break
    else:
       print(n,"is a prime number")




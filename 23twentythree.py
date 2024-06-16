# Write a program that can multiply 2 numbers provided by the user without using the * operator

a=int(input("enter first number:"))
b=int(input("Enter second number:"))
mul=0
for i in range(1,b+1):
    mul=mul+a
print(mul)

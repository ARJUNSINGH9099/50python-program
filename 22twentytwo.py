# Write a program to find the sum of first n numbers, where n will be provided by the user. Eg if the user provides n=10 the output should be 55.

n= int(input("enter the number:"))
a=0
for i in range(1,n+1):
    a=a+i
print("sum of all integer is=",a)
# Write a program to calculate the sum of the following series till the nth term
# 1/1! + 2/2! + 3/3! + 4/4! +��.+ n/n!
# n will be provided by the user

n=int(input("enter the number:"))
fact=1
result=0
for i in range(1,n+1):
    fact=fact*i
    result=result+(i/fact)
print(result)
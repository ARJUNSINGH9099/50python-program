#  Write a program to find the compound interest�

p=int(input("enter ammount:"))
r=int(input("Enter interest rate:"))
t=int(input("enter years in months:"))

a=p*(1+r/100)**t
print("Your ammount is ",a)
ci=a-p
print("your compund interest is",ci)
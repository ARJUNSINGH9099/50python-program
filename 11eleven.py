# 11. Write a program to find the simple interest when the value of principle,rate of interest and time period is given.

price=float(input("Enter the ammount:"))
rate_of_interest=float(input("Enter interest rate:"))
year=float(input("enter years:"))

simple_interest=(price*rate_of_interest*year)/100
print("your simple interest is ",simple_interest)
x=price+simple_interest
print("your total ammount is ",x," after ",year," year")

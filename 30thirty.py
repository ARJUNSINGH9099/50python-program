# User will provide 2 numbers you have to find the HCF of those 2 numbers

# solution:
# Step 1: Divide the larger number by the smaller number first, such as;
#                Larger Number/Smaller Number

# Step 2: Divide the divisor of step 1 by the remainder left.
#            Divisor of step 1/Remainder

# Step 3: Again divide the divisor of step 2 by the remainder.
#             Divisor of step 2/Remainder

# Step 4: Repeat the process until the remainder is zero.
# Step 5: The divisor of the last step is the HCF

a=int(input("enter the number:"))
b=int(input("Enter the number"))

while a%b!=0:
    rem=a%b
    a=b
    b=rem
print("your hcf is:" ,b)



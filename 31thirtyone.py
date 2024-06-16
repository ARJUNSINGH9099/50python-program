# User will provide 2 numbers you have to find the by LCM of those 2 numbers

a=int(input("enter the number:"))
num_1=a
b=int(input("Enter the number:"))
num_2=b
while num_1%num_2!=0:
    rem=num_1%num_2
    num_1=num_2
    num_2=rem
hcf=num_2
lcm=(a*b)/hcf
print("your lcm of",a,"and",b,"is:",lcm)
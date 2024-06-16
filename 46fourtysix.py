# <!-- The natural logarithm can be approximated by the following series.

# If x is input through the keyboard, write a program to calculate the sum of the first seven terms of this series. -->
# (x-1)/x+1/2(x-1/x)**2+1/2(x-1/x)**3..........+1/2(x-1/x)**7

x=int(input("enter the number:"))
n=7
sum=((x-1)/x)

for i in range(2,n+1):
    sum=sum+(1/2*((x-1)/x)**i)
print(sum)
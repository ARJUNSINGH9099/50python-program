# Write a program that will take three digits from the user and add the square of each digit.
# Write a program that will check whether the number is armstrong number or not.
n=int(input("enter the three digit number:"))
temp=n
s=0
for i in range(0,1000):
    while n!=0:
        r=n%10
        s=s+r**3     #if we want square then we put 2 instead of 3
        n=n//10
    print(s)

if temp==s:
    print("armstronge")
else:
    print("not armstrong")
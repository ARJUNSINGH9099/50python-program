# # problem:Write a program that will give you the sum of 3 digits


a=int(input("enter the number:"))

x=a%10    #if a=125 then 125%10=5

w=a//10   #w=125//10  w=12

y=w%10    #y=12%10   y=2

z=w//10    #z=12//10  z=1

sum=(x+y+z)

print(sum)


    


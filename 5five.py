# Write a program that will reverse a four digit number.Also it checks whether the reverse is true.

# x=int(input("enter a number:"))
# y=x
# a=y%10

# y=x//10
# b=y%10

# y=y//10
# c=y%10

# y=y//10
# d=y%10

# result=1000*a+100*b+10*c+d
# print(result)

# # check
# if result!=x:
#     print("true")
# else:
#     print("false")



    # ================another way

n=int(input("enter a number:"))
reverse=0
while n>0:
    a=n%10
    reverse=reverse*10+a
    n=n//10
print(reverse)

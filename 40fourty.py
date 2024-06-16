# 27. Write a program to print the following pattern
# *
# **
# ***
# **
# *

n=int(input("enter the number:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
for k in range(1,i+1):
    for l in range(1,n-k+1):
        print("*",end="")
    print()


# 26. Write a program to print the following pattern
# *
# **
# ***
# ****
# *****


n=int(input("Enter number:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
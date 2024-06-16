#  Write� a program to print the following pattern
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *


n =int(input("enter the number:"))

for i in range(1, n + 1):
    for j in range(1, n-i+1):
        print(' ', end=' ')
    for k in range(n-i+1,n+i):
        print("*",end=" ")
    print()
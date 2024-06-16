#problem: User will input (2numbers).Write a program to swap the numbers
a=int(input("enter first number:"))
b=int(input("enter second number:"))
print("before swapping a is:",a,"before swapping b is:",b)

temp=a
a=b
b=temp
print("after swapping a is :",a,"after swapping b is :",b)

# without using third variable we using a built in function

print("before swapping a is:",a,"before swapping b is:",b)
a,b=b,a
print("after swapping a is :",a,"after swapping b is :",b)
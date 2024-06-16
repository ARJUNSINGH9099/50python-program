# Write a program that will give you the in hand salary after deduction of HRA(10%),DA(5%),PF(3%), 
# and tax(if salary is between 5-10 lakh�10%),(11-20lakh�20%),(20< _ � � 30%)(0-1lakh print k).


salary=float(input("enter total salary:"))

if salary>=0 and salary<=100000:
    print("salary is",salary)
if salary>=1100000 and salary<=2000000:
    tax=salary*20/100
    salary=salary-tax
    
if salary>=500000 and salary<=1000000:
    tax=salary*10/100
    salary=salary-tax
if salary>2000000:
    tax=salary*40/100
    salary=salary-tax
print("salary after detuction tax",salary)

hra=salary*10/100
da=salary*5/100
pf=salary*3/100
inHandSalary=salary-hra-da-pf
print("Employee in hand salary",inHandSalary)


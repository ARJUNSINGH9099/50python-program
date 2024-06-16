# Print the first 20 numbers of a Fibonacci series.
l=[]
a=-1
b=1
count=0
# print(a)
# print(b)
while True:
    c=a+b
    a=b
    b=c
    l.append(c)

    count+=1
    if count==20:
        break
print(l)
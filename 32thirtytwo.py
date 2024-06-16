# Print first 25 prime numbers
l=[]
num=2
count=0
while count<=25:
    for i in range(2,num):
        if num%i==0:
            break
    else:
        # print(num)
        l.append(num)
        count+=1
    num=num+1
print(l)
    
    

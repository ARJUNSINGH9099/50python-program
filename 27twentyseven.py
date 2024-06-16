# Print all the armstrong numbers in the range of 100 to 1000in
# n=int(input("enter the number:"))
arm=0
# temp=n
for num in range(100,10000):
    i=num
    a=num%10
    num=num//10
    b=num%10
    c=num//10
    z=a**3+b**3+c**3
    if z==i:
       print(i)
    i+=1


    

    
    
    
    



 
   
            
             
# print(arm)
# if i==arm:
#     l.append(arm)
# print(l)
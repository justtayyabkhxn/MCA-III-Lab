import math
a=int(input("Enter start point of range: "))
b=int(input("Enter end point of range: "))
for i in range(a,b+1):
    flag=False
    for j in range(2,int(math.sqrt(i)+1)):
        if (i%j)==0:
            flag=True
            break
    if flag==False:
        print(i)
        
        

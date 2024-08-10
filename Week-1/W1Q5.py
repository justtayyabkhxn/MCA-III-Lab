import math
n=int(input("Enter the number to which you need sum: "))
for i in range(1,n+1):
    print(f"{i} : {int(math.pow(i,3))}")
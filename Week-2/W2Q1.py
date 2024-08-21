n=int(input("Enter a number: "))
list=[]
while (n>0) :
    list.append(n%10)
    n=(n//10)
print(list)
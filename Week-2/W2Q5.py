n=int(input("Enter a number: "))
ans=0
while (n>0) :
    ans+=n%10
    n=(n//10)
print(ans)
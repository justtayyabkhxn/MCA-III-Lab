#Write a program to count the number of occurrences of item 50 from belowtuple tp1:

mytuple= (50, 10, 60, 70, 50,50, 10, 60, 70, 50,50, 10, 60, 70, 50,50, 10, 60, 70, 50)
ans=0

for i in mytuple:
    if  i==50:
        ans+=1
print(ans)

n=int(input("Enter the last number for sum: "))
n+=1
sum=0
#METHOS 1
for x in range(1,n):
    sum+=x
print("The sum using itertaion is: ",sum)
    
#METHOD 2
print(f"The sum using formula is: {int(n*(n-1)/2)}")


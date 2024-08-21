n=int(input("Enter the number for factorial: "))
fact=1
x=n
while n!=0:
    fact=fact*n
    n-=1
print(f"Factorial of {x} is: {fact}")
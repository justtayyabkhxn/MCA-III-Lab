print("Enter 20 numbers: ")
ans=[]

for i in range(0,20):
    num=int(input(f"Enter element {i+1}: "))
    if num%5==0:
        ans.append(num)

print(ans)
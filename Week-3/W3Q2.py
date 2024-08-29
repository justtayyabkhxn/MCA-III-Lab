rows=int(input("Enter the rows: "))
x=rows
for i in range(0,x):
    for j in range(0,i):
        print(f"* ",end="")
    print()
for i in range(rows,0,-1):
    for j in range(i,0,-1):
        print(f"* ",end="")
    print()
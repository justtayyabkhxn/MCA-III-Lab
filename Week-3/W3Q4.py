str=input("Enter the word: ")
l=list(str)
print(l)
for i in range(0,len(l)):
    if i%2==0:
        print(l[i])
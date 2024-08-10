num=(input("Enter the number : "))
l1=num.split()
l2=num[::-1].split()
print(l2)
if l1==l2:
    print("Pallindrome")
else:
    print("Not Pallindrome")
#Given a two Python list. Write a program to iterate both lists simultaneouslyand display items from list 1 in original order and items from list 2 in reverse order.

list1=[1, 4, 9, 36, 25, 16, 25, 36, 9, 441, 16, 25, 81, 64, 49, 1]
list2=[1,2,3,6,5,4,5,6,3,21,4,5,9,8,7,1]

for i in range (0,16):
    print(list1[i],end=" ")
    print(list2[-1-i])

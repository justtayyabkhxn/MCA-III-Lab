#Write a function to return True if the first and last number of a given list issame. If numbers are different then return False.


def checkVal(mylist):
    if mylist[0]==mylist[-1]:
        return True
    return False

mylist=[1,2,3,6,5,4,5,6,3,21,4,5,9,8,7,1]

print(checkVal(mylist)) 


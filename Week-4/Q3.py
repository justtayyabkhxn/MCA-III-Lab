#Given a list of numbers. Write a program to turn every item of a list into its square

mylist=[1,2,3,6,5,4,5,6,3,21,4,5,9,8,7,1]
print(list(map(lambda x: x*x,mylist)))

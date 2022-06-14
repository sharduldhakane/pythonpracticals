# Author: Riddhish V. Lichade
# Program to print array elements in reverse order

l=eval(input("Enter a list: "))
length=len(l)
print("Array elements in reverse are: ")
for i in range(-1,-length-1,-1):
    print(l[i],end=' ')
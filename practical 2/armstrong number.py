# Author: Shardul N. Dhakane
# Program to check if a given number is armstrong number or not

n=int(input("Enter a number: "))
sum=0
for i in str(n):
    sum+=int(i)**3
if sum==n:
    print("The given number is armstrong number")
else:
    print("The given number is not a armstrong number")

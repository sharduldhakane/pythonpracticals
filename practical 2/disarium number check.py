# Author: Shardul N. Dhakane
# Program to check if a given number is disarium number or not

n=int(input("Enter a number: "))
ans=0
for i in range(len(str(n))):
    ans+=int(str(n)[i])**(i+1)
if(ans==n):
    print(n," is a disarium number")
else:
    print(n,"is not a disarium number")

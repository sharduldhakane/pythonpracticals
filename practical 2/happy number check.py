# Author: Riddhish V. Lichade
# Program to check if a number is happy number or not
def sumofsqofdig(n):
    s=0
    for i in str(n):
        s+=int(i)*int(i)
    return s

n=int(input("Enter a number: "))
ans=sumofsqofdig(n)
while ans!=1 and ans!=4:
    ans=sumofsqofdig(ans)

if ans==1:
    print(n," is a happy number")
else:
    print(n," is not a happy number")
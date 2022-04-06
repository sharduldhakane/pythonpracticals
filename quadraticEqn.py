# Author: Riddhish V. Lichade
# Python program to solve quadratic equation
import math
print("This python program helps to find the roots of quadratic equation")
print("A quadratic equation is of the format ax^2 + bx + c =0\n Kindly enter the values of a,b,c:")
a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))
D=(math.pow(b,2)-(4*a*c))
if(D<0):
    print("The roots of the quadratic equation",a,"x^2 +",b,"x +",c,"are imaginary",sep="")
    exit()
b*=-1
root1=(b+D)/(2*a)
root2=(b-D)/(2*a)
print("The roots of the quadratic equation",a,"x^2 +",b,"x +",c,"are",root1,"and",root2,sep="")

# Author: Riddhish V. Lichade
# Program to find length of list using recursion

from sys import stdin, stdout, setrecursionlimit
def inlist(): return list(map(str, stdin.readline().strip().split()))

def lengthOfList(l):
    length += 1
    if l:
        lengthOfList(l[1::])


print("This is a python program to find length of list using recursion ")
print("-------------------------------------------------------------------------------------\n")
print("Enter the elements of list seperated by space: ")
l = inlist()
global length=0
print("Length of the given list is ", length)

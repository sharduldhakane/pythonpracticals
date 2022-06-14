# Author: Riddhish V. Lichade
# username: root_rvl

from collections import Counter, defaultdict
from sys import stdin, stdout, setrecursionlimit
from heapq import nlargest, nsmallest
import math
setrecursionlimit(2147400000)
def outnl(x): stdout.write(str(x)+'\n')
def outsl(x): stdout.write(str(x)+' ')
def instr(): return stdin.readline().strip()
def inint(): return int(stdin.readline())
def inspsint(): return map(int, stdin.readline().strip().split())
def inlist(): return list(map(int, stdin.readline().strip().split()))

for _ in range(inint()):
    
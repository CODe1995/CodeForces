##########################################################
import sys
input = sys.stdin.readline
def ii():return int(input())
def mii():return map(int,input().rstrip().split())
def lmii():return list(map(int,input().rstrip().split()))
##########################################################
from math import ceil
t = ii()
for _ in range(t):
    a,b,c = mii()
    mx = max(a,b,c)
    mx = mx//7
    s = a+b+c
    if s%9==0 and a>=mx and b>=mx and c>=mx:
        print('YES')
    else:
        print('NO')
##########################################################
import sys
from collections import deque
input = sys.stdin.readline
# print = sys.stdout.write
def ip():return input().rstrip()
def ii():return int(input())
def mii():return map(int,input().rstrip().split())
def lmii():return list(map(int,input().rstrip().split()))
##########################################################

t = ii()
for _ in range(t):
    n = ii()
    A = list(map(int,list(ip())))
    B = list(map(int,list(ip())))
    awin = 0
    bwin = 0
    for i in range(n):
        if A[i] < B[i]:
            bwin+=1
        elif A[i]>B[i]:
            awin+=1
    if awin>bwin:print('RED')
    elif awin<bwin:print('BLUE')
    else:print('EQUAL')
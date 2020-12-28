##########################################################
import sys
input = sys.stdin.readline
def ip():return input().rstrip()
def lip():return list(input().rstrip())
def ii():return int(input())
def mii():return map(int,input().rstrip().split())
def lmii():return list(map(int,input().rstrip().split()))
##########################################################
from collections import deque
t = ii()
for _ in range(t):
    arr = lip()
    stat = 0
    for i in range(len(arr)):
        c=arr[i]
        if c=='(':
            stat+=1
        elif c==')':
            stat-=1
        else:
            if i+1 < len(arr):
                if stat-1 ==0 and arr[i+1]==')':
                    stat+=1
                    continue
            if stat==0:stat+=1
            else:stat-=1        
        if stat<0:
            break
    # print('stat:',stat)
    if stat==0:
        print('YES')
    else:print('NO')
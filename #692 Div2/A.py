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
    n =ii()
    arr = ip()
    cnt=0
    for i in range(n-1,-1,-1):
        if arr[i]==')':
            cnt+=1
        else:break
    if 2*cnt>n:print('YES')
    else:print('NO')
            
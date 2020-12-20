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
    endPoint = 0
    for i in range(n):
        if arr[i:] == ')'*(n-i):
            # print(n-i,i)
            break
    if i>=n-i:print('NO')
    else:print('YES')
            
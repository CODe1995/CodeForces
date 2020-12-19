##########################################################
import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write
def i():return input().rstrip()
def ii():return int(input())
def mii():return map(int,input().rstrip().split())
def lmii():return list(map(int,input().rstrip().split()))
##########################################################
def gcd(a,b):#if a>b
    if a<b:a,b=b,a
    while True:
        r = a%b
        if r==0: return b
        a=b
        b=r


n,m = mii()
A = lmii()
B = lmii()
prev = 1
cur = 0
for j in range(m):
    abcnt=0
    for i in range(n):
        cur = A[i]+B[j]
        abcnt+=1
        if abcnt>1:
            prev=gcd(prev,cur)
            # print(i,j,prev,cur)
        else:prev=cur
    print(str(prev)+' ')
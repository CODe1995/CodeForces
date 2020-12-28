##########################################################
import sys
input = sys.stdin.readline
def ip():return input().rstrip()
def lip():return list(input().rstrip())
def ii():return int(input())
def mii():return map(int,input().rstrip().split())
def lmii():return list(map(int,input().rstrip().split()))
##########################################################
t = ii()
for _ in range(t):
    n,a,m,b = ii(),lmii(),ii(),lmii()
    for i in range(1,n):
        a[i]+=a[i-1]
    for i in range(1,m):
        b[i]+=b[i-1]
    resA = max(a)
    resB = max(b)
    if resA<0:resA=0
    if resB<0:resB=0
    print(resA+resB)
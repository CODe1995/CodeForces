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
    graph = dict()
    n,m = mii()
    parent = [i for i in range(n+1)]
    def getParent(x):
        if parent[x]==x:return x
        parent[x] = getParent(parent[x])
        return parent[x]
    def unionParent(x,y):
        x=getParent(x)
        y=getParent(y)
        if x==y: return 1
        parent[x]=y
        return 0
    res = 0
    for i in range(m):
        x,y = mii()
        if x==y:continue
        res+=1+unionParent(x,y)
    print(res)
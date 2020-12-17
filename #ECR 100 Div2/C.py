##########################################################
import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write
def ii():return int(input())
def mii():return map(int,input().rstrip().split())
def lmii():return list(map(int,input().rstrip().split()))
##########################################################
t = ii()
for _ in range(t):
    n = ii()
    q = deque()
    for _ in range(n):
        a,b = mii()
        q.append([a,b])
    ans = 0#answer cnt
    cur = 0#current robot position
    cmdidx = 0#command index
    goalidx = 0#goal index
    while q:
        moveTime = abs(q[cmdidx][1]-cur)+q[cmdidx][0]#move time
        #ignore part
        ignoreCmd = cmdidx+1#ignored cmd counts
        while n>ignoreCmd and q[ignoreCmd][0]<=moveTime:
            ignoreCmd+=1


        while True:
            if cur<=q[goalidx][1]<=q[cmdidx][1] and abs(cur-q[goalidx][1])<q[-1][0]:
                ans+=1
                goalidx+=1
            if cmdidx+ignoreCmd<=goalidx:
                break
        cur = q[cmdidx][1]
        cmdidx += ignoreCmd
        
        if cmdidx > n:
            break
    print(ans)

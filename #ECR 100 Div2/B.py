##########################################################
import sys
input = sys.stdin.readline
print = sys.stdout.write
def ii():return int(input())
def mii():return map(int,input().rstrip().split())
def lmii():return list(map(int,input().rstrip().split()))
##########################################################
t = ii()
for _ in range(t):
    n = ii()
    arr = lmii()
    S = sum(arr)
    mid = S//n
    ans = [mid]*n
    for _ in range(n):
        print(str(mid)+" ")
    print("\n")
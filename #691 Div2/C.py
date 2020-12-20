##########################################################
import sys,math
from collections import deque
input = sys.stdin.readline
# print = sys.stdout.write
def i():return input().rstrip()
def ii():return int(input())
def mii():return map(int,input().rstrip().split())
def lmii():return list(map(int,input().rstrip().split()))
##########################################################
n,m = mii()
a = lmii()
b = lmii()
var = 0
for i in range(1,n):
    print("gcd(%d, a[%d]%d-a[0]%d)"%(var,i,a[i],a[0]))
    var = math.gcd(var,a[i]-a[0])
for i in b:
    print("gcd(%d, i%d+a[0]%d)"%(var,i,a[0]))
    print(math.gcd(var,i+a[0]),end=" ")
print()
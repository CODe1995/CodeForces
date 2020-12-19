##########################################################
import sys
from collections import deque
input = sys.stdin.readline
# print = sys.stdout.write
def i():return input().rstrip()
def ii():return int(input())
def mii():return map(int,input().rstrip().split())
def lmii():return list(map(int,input().rstrip().split()))
##########################################################

n = ii()
if n%2==0:
    print((n//2+1)*(n//2+1))
else:
    print(((n+1)//2)*((n+1)//2+1)*2)
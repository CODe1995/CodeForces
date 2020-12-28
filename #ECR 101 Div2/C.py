##########################################################
import sys
input = sys.stdin.readline
def ip():return input().rstrip()
def lip():return list(input().rstrip())
def ii():return int(input())
def mii():return map(int,input().rstrip().split())
def lmii():return list(map(int,input().rstrip().split()))
sys.setrecursionlimit(10**7)
##########################################################
t = ii()
for _ in range(t):
    n,k = mii()
    arr = lmii()
    
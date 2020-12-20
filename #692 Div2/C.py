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
    # field = [[0]*n for _ in range(n)]
    arr = list()
    for i in range(m):
        x,y = mii()
        if x in graph:
            graph[x].append([x,y])
        else:
            graph[x]=[[x,y]]
        if y in graph:
            graph[y].append([x,y])
        else:
            graph[y]=[[x,y]]
    
    for nodes in graph:
        for i,node in enumerate(graph[nodes]):
            if len(graph[node[0]])==1:#해당 구역에 혼자라면
                graph[nodes][i]=
        
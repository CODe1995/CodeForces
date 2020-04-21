import sys
input = sys.stdin.readline

t = int(input())
while t:
    t-=1
    n,m,a,b,c=map(int,input().split())
    weights = list(map(int,input().split()))
    track=[]
    for i in range(m):
        track.append(list(map(int,input().split())))

    
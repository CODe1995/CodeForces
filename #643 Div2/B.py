import sys
input = sys.stdin.readline

t= int(input())
while t:
    t-=1
    e = int(input())
    arr = list(map(int,input().strip().split()))
    arr = sorted(arr)
    ans = 0
    cur = 0
    i=0
    while i<len(arr):
        cur+=1
        if cur==arr[i]:
            ans+=1
            cur=0
        i+=1
    print(ans)
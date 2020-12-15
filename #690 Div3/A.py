import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().rstrip().split()))
    s,e=0,n-1
    
    while s<=e:
        if s!=e:
            print(arr[s],arr[e],end=' ')
        else:
            print(arr[s],end='')
        s+=1
        e-=1
    print()
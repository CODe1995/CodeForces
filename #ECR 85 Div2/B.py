import sys
inp = sys.stdin.readline

t = int(inp())

while t:
    t-=1
    n,x = map(int,inp().split())
    arr = list(map(int,inp().split()))
    arr = sorted(arr,reverse=True)

    for i in range(1,n):
        arr[i]=arr[i-1]+arr[i]
    print(arr)
    if arr[-1]/n >= x:
        print(n) 
    elif arr[0]<x:
        print(0)
    else:
        for i in range(n):
            if arr[i]/(i+1)<x:
                print(i)
                break
                

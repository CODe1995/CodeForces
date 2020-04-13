import sys,math
inp = sys.stdin.readline


t = int(inp())
while t:
    t-=1
    n = int(inp())
    tmp=[]
    arr=list(map(int,inp().split()))
    arr= sorted(arr,reverse=True)
                 
    
    right = n//2
    left = right-1
    while left >-1 or right<n:
        if right<n:
            print(arr[right],end=' ')
            right+=1
        if left>-1:
            print(arr[left],end=' ')
            left-=1
    print()
    
    # print(a)  
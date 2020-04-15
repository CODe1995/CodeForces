import sys

input = sys.stdin.readline

t = int(input())
left =0
right = 0
mid = 0
while t:
    ans = []
    t-=1
    n = int(input())
    arr=list(map(int,input().split()))
    
    right = len(arr)//2
    left = right-1

    if len(arr)%2!=0:        
        right+=1

    cnt = 0
    while arr[left]==arr[right]:
        cnt +=1
        if left>-1:
            left-=1
        if right<len(arr):
            right+=1
    
    ans.append(cnt)



    print(max(ans))
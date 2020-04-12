import sys,math
inp = sys.stdin.readline


t = int(inp())
while t:
    t-=1
    n = int(inp())
    tmp=[]
    arr=list(map(int,inp().split()))
    arr= sorted(arr)
    turn = 0
    if arr[0]<0:                
        if len(arr)%2==0:
            right = len(arr)//2
            left = right-1
            while right<len(arr):
                if turn==1:
                    tmp.append(arr[left])
                    tmp.append(arr[right])
                    turn=0
                else:                    
                    tmp.append(arr[right])
                    tmp.append(arr[left])
                    turn=1
                left-=1
                right+=1
        else:            
            right = len(arr)//2
            left = right-2
            tmp.append(arr[right-1])
            while right<len(arr):
                if turn==0:
                    tmp.append(arr[left])
                    tmp.append(arr[right])
                    turn=1
                else:                    
                    tmp.append(arr[right])
                    tmp.append(arr[left])
                    turn=0
    else:
        tmp=arr
    for i in tmp:
        print(i,end=' ')
    print()
    # print(a)  
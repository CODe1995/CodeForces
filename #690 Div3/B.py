import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = input().rstrip()
    ans=False
    if len(arr)>4:
        for i in range(n):        
            for j in range(i,n):
                if arr[:i]+arr[j+1:] == "2020":
                    print("YES")
                    ans= True
                    break
            if ans==True:break
        if ans==False:
            print('NO')
    else:
        if arr=='2020':
            print('YES')
        else:
            print('NO')
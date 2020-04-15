import sys
input = sys.stdin.readline
arr = []

t = int(input())
while t:
    t-=1

    n = int(input())
    arrA = list(map(int,input().split()))
    arrB = list(map(int,input().split()))
    minus = 0
    plus = 0
    ans = 'NO'
    
    for i in range(n):
        if i>0:
            if arrA[i-1]<0 and minus==0:
                minus=1
            elif arrA[i-1]>0 and plus==0:
                plus=1
        if arrA[i]<arrB[i] and plus==1:
            ans='YES'
        elif arrA[i]>arrB[i] and minus==1:
            ans='YES'
        elif arrA[i]==arrB[i]:
            ans='YES'
        else:
            ans='NO'
            break                
    print(ans)




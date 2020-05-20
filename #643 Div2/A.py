import sys
input = sys.stdin.readline

t = int(input())
arr=[]
ans=[]
dp=[0,0]
#seq,result
def calc(a,k):    
    if dp[0]>0 and ('0' in str(dp[1])):
        return dp[1]

    while dp[0]!=k-1:
        if dp[0]>0:
            dp[0]+=1
            dp[1]=dp[1]+min(map(int,list(str(dp[1]))))*max(map(int,list(str(dp[1]))))
        else:
            dp[0]+=1
            dp[1]=a+min(map(int,list(str(a))))*max(map(int,list(str(a))))
    return dp[1]

for i in range(t):
    a,k=map(int,input().strip().split())
    arr.append([i,a,k])

arr=sorted(arr,key=lambda x:[x[1],x[2]])
ans=[]

for i in range(t):
    if t>1 and i>=1:
        if arr[i-1][1]!=arr[i][1]:
            dp=[0,0]
    if arr[i][2]==1:
        ans.append([arr[i][0],arr[i][1]])
    else:
        ans.append([arr[i][0],calc(arr[i][1],arr[i][2])])
ans=sorted(ans,key=lambda x:x[0])
for i in ans:
    print(i[1])
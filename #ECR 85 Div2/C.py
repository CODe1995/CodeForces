import sys
inp = sys.stdin.readline

t = int(inp())
circle = []
while t:
    t-=1
    n = int(inp())
    dp = [[0,0] for _ in range(300000)]
    
    for i in range(n):        
        circle.append(list(map(int, inp().split())))        
        if i==n-1:            
            dp[0][0]=circle[0][0]
            dp[0][1]=circle[0][0]-circle[i][1]
            dp[i][0]=circle[i][0]
            dp[i][1]=circle[i][0]-circle[i-1][1]
        elif i>=1:
            dp[i][0]=circle[i][0]
            dp[i][1]=circle[i][0]-circle[i-1][1]
    ans = []
    
    for i in range(n):        
        cnt = dp[i][0]
        for j in range(i+1,n):
            if dp[j][1]>0:
                cnt+=dp[j][1]
        for j in range(0,i):            
            if dp[j][1]>0:
                cnt+=dp[j][1]
        ans.append(cnt)
    print(min(ans))
    
        




    

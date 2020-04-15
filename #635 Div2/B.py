import sys
import math
input = sys.stdin.readline
dp=[[[0 for _ in range(31)] for _ in range(30+1)] for _ in range(10**5+1)]

def skill1(h):    
    return math.floor(h/2)+10
def skill2(h):
    return h-10


#1 = succ
#2 = fail
def calc(h,n,m):   
    if  dp[h][n][m] != 0:
        return dp[h][n][m]

    if h<=0:
        dp[h][n][m]=1
        return dp[h][n][m]        
    elif m==0 and n==0:
        dp[h][n][m]=2
        return dp[h][n][m]    
    if n>0:        
        # if m==0:
        #     dp[h][n][m] = 2            
        #     return dp[h][n][m]
        dp[h][n][m] = calc(skill1(h),n-1,m)        
        return dp[h][n][m]
    if m>0:
        # if (n==0 and h-10*m>0):
        #     dp[h][n][m] = 2            
        #     return dp[h][n][m]
        # else:
            dp[h][n][m] = calc(skill2(h),n,m-1)    
            return dp[h][n][m]
        
t = int(input())

while t:
    t-=1
    x,n,m = map(int,input().split())
    calc(x,n,m)
    if dp[x][n][m]==1:
        print('YES')
    else:
        print('NO')
    # print(dp[x][n][m])
    
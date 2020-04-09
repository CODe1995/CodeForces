import sys
inp = sys.stdin.readline

n = int(inp().strip())
arr = list(map(int,inp().split()))
sumarr = list()
sumarr.append(arr[0])
cnt = n

for i in range(1,n):
    sumarr.append(sumarr[i-1]+arr[i])
    

minus = sumarr.count(0)
value = 0
ans = 0
if sumarr[-1] == 0:
    value = -1
    minus -=1

for i in range(len(sumarr)-minus,0,-1):
    ans+=i

print(ans+value)
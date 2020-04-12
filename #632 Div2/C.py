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

# import io, os
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
# for t in range(int(input())):
#     n = int(input())
#     A = [0]*n
#     B = [0]*n
#     for i in range(n):
#         A[i], B[i] = [int(s) for s in input().split()]
#     minB = B[0]
#     ans = 0
#     for i in range(-1,n-1):
#         if B[i] > A[i+1]:
#             B[i] = A[i+1]
#         minB = min(minB,B[i])
#         ans += (A[i]-B[i])
 
#     ans += minB
#     print(ans)
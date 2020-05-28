import sys
input=sys.stdin.readline

N = 100100
n,A,R,B = map(int,input().split())
M=0
M = min(M,A+R)
h=[0]*N
pref=[0]*N

def solve(H):
    #...

for i in range(n):
    h[i] = int(input().strip())
h=sorted(h[:n])
for i in range(n):
    pref[i+1]=pref[i]+h[i]
ans = min(ans,solve(pref[n]/n))
ans = min(ans,solve(pref[n]/n+1))
for i in range(n):
    ans = min(ans,solve(h[i]))
print(ans)

    
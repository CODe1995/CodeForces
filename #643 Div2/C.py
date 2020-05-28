import sys
input = sys.stdin.readline
A, B, C, D = map(int, input().strip().split())
N = 10**6+77
cnt = 0
a = [0]*N
for i in range(A, B+1):
    # print('i:',i,'\ni+B :',i+B,'\ni+C+1',i+C+1)
    a[i + B] += 1
    a[i + C + 1] -= 1

for i in range(1, N):
    a[i] += a[i - 1]
for i in range(1, N):
    a[i] += a[i - 1]
ans = 0 
for i in range(C, D+1):
    ans += a[N - 1] - a[i]
print(ans)
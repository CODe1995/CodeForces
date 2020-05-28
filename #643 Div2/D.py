import sys
input = sys.stdin.readline
n,s=map(int,input().strip().split())
if 2*n<=s:
    print('YES')
    for i in range(n-1):
        print(2,end=' ')
        s-=2
    print(s,'\n1')
else:
    print('NO')    
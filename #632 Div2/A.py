
import sys
inp = sys.stdin

t = int(inp.readline())

ans = []

while t:
    t-=1    
    n,m = map(int,inp.readline().split())
    for i in range(n):
        for j in range(m):
            if i==0 and j==0:
                print('W',end='')
            else:
                print('B',end='')
        print()

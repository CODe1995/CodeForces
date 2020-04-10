import sys
inp = sys.stdin.readline

t = int(inp())

while t:
    t-=1
    n = int(inp())
    bp=0
    bc=0
    flag = True
    while n:
        n-=1
        p,c = map(int,inp().split())
        if p<bp or c<bc or bc-c<bp-p:
            flag = False
        bp,bc = p,c
    if flag==True:
        print('YES')
    else:
        print('NO')
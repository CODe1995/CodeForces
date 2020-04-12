import sys
inp = sys.stdin.readline


t = int(inp())
while t:
    t-=1
    n=int(inp())
    if n<=2:
        print(n)
    else:
        print(2*(n-1)*(n))
    
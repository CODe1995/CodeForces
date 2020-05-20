import sys
input = sys.stdin.readline

def calc(x):
    m1=10
    m2=0
    while x>0:
        y = x%10
        x//=10
        m1=min(m1,y)
        m2=max(m2,y)
    return m1*m2

t = int(input())
while t:
    t-=1
    x,k = map(int,input().strip().split())
    k-=1
    while k:
        k-=1
        y = calc(x)
        if y==0:break
        x+=y
    print(x)
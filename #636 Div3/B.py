import sys
input = sys.stdin.readline

t = int(input())
while t:
    t-=1
    n=int(input())
    hol=[]
    jak=[]
    if (n//2)%2==0:
        print('YES')
        for i in range(n//2):
            jak.append(2*(i+1))
        for j in range(n//2-1):
            hol.append(2*(j+1)-1)
        hol.append(sum(jak)-sum(hol))        
        for i in jak:print(i,end=' ')
        for i in hol:print(i,end=' ')
        print()
    else:
        print('NO')
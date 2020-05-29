import sys
input = sys.stdin.readline
t=int(input().strip())

while t:
    ans=0
    t-=1
    n,m,x,y=map(int,input().split())
    field=list('.'*m for _ in range(n))
    
    for i in range(n):
        field[i]=list(input().strip())

    if 2*x<=y:
        for i in range(n):
            for j in range(m):
                if field[i][j]=='.':
                    ans+=x
    else:
        for i in range(n):
            j=0
            while j+1<=m:
                if field[i][j:j+2]==['.','.']:
                    j+=1
                    ans+=y
                elif field[i][j]=='.':
                    ans+=x
                j+=1
    print(ans)
                
            




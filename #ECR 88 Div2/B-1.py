import sys
from collections import deque
input = sys.stdin.readline
t=int(input().strip())


while t:
    ans=0
    t-=1
    n,m,x,y=map(int,input().split())
    field=list('.'*m for _ in range(n))
    
    for i in range(n):
        field[i]=list(input().strip())

    if x<y:
        for i in range(n):
            for j in range(m):
                if field[i][j] == '.':
                    ans+=x
        print(ans)
    else:
        for i in range(n):
            for j in range(m-1):
                if field[i][j:j+2]==['.','.']:
                    ans+=y
                    field[i][j:j+1]=['*','*']        
        for i in range(n-1):
            for j in range(m):
                if [['.'],['.']] in field[i:i+2][j]:
                    ans+=y
                    field[i:i+1][j]=[['*'],['*']]
        for i in range(n):
                for j in range(m):
                    if '.' in field[i][j]:
                        ans+=x
                        field[i][j]='*' 
        
        print(ans)

            
            




import sys
from collections import deque
input = sys.stdin.readline
t=int(input().strip())
direction = [[0,1],[1,0],[0,-1],[-1,0]]
nextq = deque()
def bfs(field, valid):    
    while nextq:
        vx,vy=nextq.popleft()        
        for dx,dy in direction:
            tx = vx+dx
            ty = vy+dy
            if tx>=0 and tx<m and ty>=0 and ty<n and valid[ty][tx]==0:
                if field[ty][tx] == '.':
                    nextq.append([tx,ty])
    return 0

while t:
    ans=0
    t-=1
    n,m,x,y=map(int,input().split())
    field=list('.'*n for _ in range(m))
    valid=list([0]*n for _ in range(m))
    
    for i in range(m):
        field[i]=list(input().strip())
    if x<y:
        for i in field:
            for j in i:
                if j == '.':
                    ans+=1
        print(ans)
    else:
        for i in range(n):
            for j in range(m):
                bfs(field,valid,[j,i])

            
            




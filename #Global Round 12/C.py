import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write
direction_5 = [[0,1,2,3,6],[6,0,3,7,8],[8,2,5,7,6],[2,0,1,5,8],[3,0,6,4,5],[7,6,8,4,1],[5,4,3,2,8],[1,0,2,4,7],[4,1,3,5,7]]
direction_3 = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8]]
t = int(input())
for _ in range(t):
    n = int(input())    
    k=0
    field= []
    
    for _ in range(n):
        tmp = list(input().rstrip())
        for i in tmp:
            if i == 'X':
                k+=1
        field.append(tmp)
    canDo = round(k/3)
    for y in range(n):
        if canDo==0:break
        for x in range(n):
            if canDo==0:break
            for a,b,c,d,e in direction_5:
                if x+2<n and y+2<n:
                    if 'X'==field[y+a//3][x+a%3]==field[y+b//3][x+b%3]==field[y+c//3][x+c%3]==field[y+d//3][x+d%3]==field[y+e//3][x+e%3]:
                        #if same three                        
                        field[y+a//3][x+a%3]='O'
                        canDo-=1
                        break
            for a,b,c in direction_3:
                if x+2<n and y+2<n:
                    if 'X'==field[y+a//3][x+a%3]==field[y+b//3][x+b%3]==field[y+c//3][x+c%3]:
                        #if same three                        
                        field[y+b//3][x+b%3]='O'
                        canDo-=1
                        break


    for i in field:
        for j in i:
            print(j)        
        print('\n')
        
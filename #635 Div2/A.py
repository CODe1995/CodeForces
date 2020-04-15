import sys
from collections import Counter
input = sys.stdin.readline
arr = []

t = int(input())
while t:
    t-=1
    a,b,c,d = map(int,input().split())
    arr = Counter([a,b,c,d]).most_common()

    if b==c:
        print(b,b,b)   
    elif arr[0][1]>=2:
        if arr[0][0]
    else:       
        done = 0 
        for x in range(a,b+1):
            for y in range(c,b,-1):
                for z in range(d,c,-1):    
                    if c>x+y:
                        break
                    if z<x+y:
                        print(x,y,z)
                        done =1
                        break
                if done==1:break                
            if done==1:break
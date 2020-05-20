import sys
input = sys.stdin.readline

a,b,c,d = map(int,input().strip().split())
cnt=0
dp=list()

for x in range(a,b+1):
    for y in range(b,c+1):
        for z in range(c,d+1):
            if x+y>z:
                cnt+=1
            else:
                break
print(cnt)
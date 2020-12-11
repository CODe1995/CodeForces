#timeLimit
import sys
input = sys.stdin.readline

stars = []
for i in range(1,500):
    if 1+((i-1)*2)>500:
        break
    stars.append('*'*(1+((i-1)*2)))

t = int(input())
for _ in range(t):
    height,width = map(int,input().rstrip().split())
    arr = []
    for _ in range(height):
        arr.append(input().rstrip())
    cnt = 0
    for i in range(height):
        for j in range(width):                
            nowLevel = 1
            while 1+(nowLevel-1)*2<=width:
                if 0<=i+nowLevel-1<height and 0<=j-(nowLevel-1)<width and 0<=j+nowLevel<=width:                    
                    if stars[nowLevel-1] == arr[i+(nowLevel-1)][j-(nowLevel-1):j+(nowLevel)]:
                        cnt+=1
                    else:
                        break
                else:
                    break
                nowLevel+=1    
    print(cnt)
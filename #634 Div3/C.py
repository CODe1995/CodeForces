import sys
from collections import Counter as counter

input = sys.stdin.readline

t = int(input())
while t:
    t-=1
    n = int(input())
    arr=list(map(int,input().split()))
    # for (i,j) in counter(arr):
    # print(counter(arr).most_common()[0])
    carr = counter(arr)
    ans = 0

    # for i in range(len(carr)):
    mostcnt = carr.most_common()[0][1]
    gou = len(carr)
    if gou==1 and mostcnt>1:
        print(gou)
    elif gou==1:
        print(0)    
    elif mostcnt-1>=gou:
        print(gou)
    elif mostcnt == gou:
        print(gou-1)
    else:
        print(mostcnt)

    

    

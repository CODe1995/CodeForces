import sys
from string import ascii_lowercase

alphalist = list(ascii_lowercase)
input = sys.stdin.readline

t = int(input())
while t:
    t-=1
    n,a,b=map(int,input().split())
    s=""
    start = 0
    while len(s)<n:
        ac = 0
        while ac<a and len(s)<n:
            for i in alphalist[start:b+start]:
                if len(s)>=n:
                    break
                s+=i; ac+=1
        start=start+b
        # while n>len(s):
        #     for i in alphalist[start:n-a+start]:
        #         if len(s)>=n:
        #             break
        #         s+=i
    print(s)
    
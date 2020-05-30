import sys
import math
input = sys.stdin.readline

t=int(input().strip())
while t:
    t-=1
    n,m,k=map(int,input().split())
    d = n // k  #한 사람당 가져가는 카드 수
    x = min(m, d)   #첫 번째 사람이 가져가는 카드의 수
    #if m>d: return d
    #else: return m
    #이렇게 써줘도 전혀 상관이 없다. 같은 방식인데 min으로하면 더 간단하다.

    y = math.ceil((m-x)/(k-1)) #남은 사람중 가져가는 카드의 최대 수
    print(x-y)
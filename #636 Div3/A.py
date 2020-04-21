import sys
input = sys.stdin.readline

t = int(input())
while t:
    t-=1
    n=int(input())
    # if n%3==0:
    #     print(n//3)
    # else:
    i=1
    while n%(3+((i-1)*4))!=0:
        i+=1
    print(n//(3+((i-1)*4)))

import sys
input = sys.stdin.readline

t = int(input())
while t:
    t-=1
    n=int(input())
    # if n%3==0:
    #     print(n//3)
    # else:    
    for i in range(1,31):
        if n%(3+((i-1)*4))==0:
            print(n//(3+((i-1)*4)))
            break
    

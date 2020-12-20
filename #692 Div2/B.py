##########################################################
import sys,math
from collections import deque
input = sys.stdin.readline
# print = sys.stdout.write
def ip():return input().rstrip()
def ii():return int(input())
def mii():return map(int,input().rstrip().split())
def lmii():return list(map(int,input().rstrip().split()))
##########################################################
def lcm(x,y):
    return x*y//math.gcd(x,y)

t = ii()
def calc(number):
    #        0,1,2,3,4,5,6,7,8,9
    check = [0,0,0,0,0,0,0,0,0,0]    
    strnum = list(str(number))
    for i in strnum:
        if i == '0':continue
        ni = int(i)
        if check[ni]==0:
            check[ni]=1            
            if ni ==1:continue
            else: 
                if number%ni==0:
                    continue
                else:
                    return 0
            # elif ni==2:
            #     if number%2==0:continue
            #     else:return 0       
            # elif ni==3:     
    return 1

for _ in range(t):
    n = ii()    
    # lenn = len(str(n))
    while True:
        if calc(n)==1:
            print(n)
            break
        else:
            n+=1
    # s,e = n,10**18
    # ans = n
    # while s<=e:
    #     mid = (s+e)//2
    #     tmp = calc(mid)
    #     if tmp==1:#every number done
    #         ans = mid   
    #     else:
    #         s+=1
    #     # print(e)
    #     print(s,e,ans)




            
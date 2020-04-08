# https://codeforces.com/contest/1330/problem/A
# 등수를 하나씩 순차적으로 수집한다.
# 경우 t가 주어지고
# 대회의 갯수 n
# 추가로 참가할 수 있는 대회의 수 x
# 대회에서 획득한 등수 ai가 주어진다.
# 최대 등수 v를 구하시오

import sys
inp = sys.stdin
arr = []

def found(num):
    for i in range(len(arr)):
        if arr[i]==num:
            return True
    return False

t = int(inp.readline())
ans = []
for i in range(t):
    a,x = map(int,inp.readline().split())
    arr = list(map(int,inp.readline().split()))
    #하단의 for문에서 최대 횟수 100 + 최대 갯수 100을 했을때 200까지 가능한데, 이걸 생각 못해서 자꾸 틀렸다.
    for j in range(1,12345):
        if found(j)==False:
            x-=1

            if x<0:
                ans.append(j-1)
                break

for i in ans:
    print(i)
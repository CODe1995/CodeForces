import sys
input = sys.stdin.readline

t = int(input())
lst = ['a','b','c']
for i in range(t):
    n,k = map(int,input().rstrip().split())
    arr = ''
    for j in range(n):
        arr += lst[j%3]
    print(arr)
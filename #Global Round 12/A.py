import sys
input = sys.stdin.readline
key = 'trygub'
keyidx = 0 
t = int(input())

for _ in range(t):
    n = int(input())
    arr = input().rstrip()
    i = 0
    while i!=len(arr):
        if key[keyidx] == arr[i]:#find 'trygub'
            if keyidx+1!=5:
                keyidx+=1
            else:#if keyidx 5
                arr = arr[i]+arr[:i]+arr[i+1:]
                i=0
                keyidx = 0
        i+=1       
    print(arr)

'''
3
11
antontrygub
15
bestcoordinator
19
trywatchinggurabruh

bugyrtnotna
bestcoordinator
bruhtrywatchinggura
'''
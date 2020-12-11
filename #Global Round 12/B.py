import sys
input = sys.stdin.readline
def calc(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    return abs(x1-x2)+abs(y1-y2)



t = int(input())
for _ in range(t):
    n,k = map(int,input().rstrip().split())
    arr = list()
    answer = [0]*n
    graph = {}
    for i in range(n):
        graph[i]=[]
    for i in range(n):
        arr.append(list(map(int,input().rstrip().split())))
        for j in range(len(arr)-1):
            if calc(arr[i],arr[j])<=k:
                if j not in graph[i]:
                    graph[i].append(j)
                if i not in graph[j]:
                    graph[j].append(i)   
    flag = False     
    for i in range(n):
        if len(graph[i])==n-1:
            print(1)
            flag=True
            break
    if flag==False:
        print(-1)
    # print(graph)
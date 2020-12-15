import sys
input = sys.stdin.readline
from math import ceil,log2
tree_max = list()
tree_min = list()
nodes = list()

#합을 출력하는 함수
def query(start,end,index,left,right):
    # 입력된 쿼리의 범위가 트리의 범위를 벗어나는 경우
    if left>end or right<start:
        return 0
    #범위 내인 경우
    if start>=left and end<=right:
        return tree[index]
    mid = (start+end)//2
    return query(start,mid,index*2,left,right)+query(mid+1,end,index*2+1,left,right)

def init_max(start,end,index):
    if start==end:
        tree_max[index] = nodes[start]
        return tree_max[index]
    mid = (start+end)//2
    tree_max[index] = max(init_max(start,mid,index*2),init_max(mid+1,end,index*2+1))
    return tree_max[index]
def init_min(start,end,index):
    if start==end:
        tree_min[index] = nodes[start]
        return tree_min[index]
    mid = (start+end)//2
    tree_min[index] = min(init_min(start,mid,index*2),init_min(mid+1,end,index*2+1))
    return tree_min[index]

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):        
        #노드수, 수의변경 수, 구간합 수
        n= int(input())
        nodes = list(map(int,input().rstrip().split()))
        h = ceil(log2(n))
        size = 2**(h+1)
        tree_max = [0]*(2**(h+1))
        tree_min = [0]*(2**(h+1))
        init_max(0,n-1,1)
        init_min(0,n-1,1)
        print(tree_max,'\n',tree_min)
        cnt=0
        for i in range(1,size):
            for j in range(i*2,size):
                for k in range(j*2,size):
                    # if max(nodes[i],nodes[j],nodes[k])-min(nodes[i],nodes[j],nodes[k])<=2:
                    if max(tree_max[i],tree_max[j],tree_max[k])-min(tree_min[i],tree_min[j],tree_min[k])<=2:                        
                        cnt+=1
        print(cnt)

        
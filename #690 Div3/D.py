import sys
input = sys.stdin.readline

tree = list()
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
#누적 합으로 트리 구성해줌
def init(start,end,index):
    if start==end:
        tree[index] = nodes[start]
        return tree[index]
    mid = (start+end)//2
    tree[index] = init(start,mid,index*2)+init(mid+1,end,index*2+1)
    return tree[index]

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        #노드수, 수의변경 수, 구간합 수
        n= int(input())
        nodes = list(map(int,input().rstrip().split()))
        tree = [0]*(n*4)
        init(0,n-1,1)
        
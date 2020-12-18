##########################################################
import sys
input = sys.stdin.readline
print = sys.stdout.write
def ii():return int(input())
def mii():return map(int,input().rstrip().split())
def lmii():return list(map(int,input().rstrip().split()))
##########################################################
'''
풀이1)해당 수를 넘지 않는 수 중 가장 큰 2의 제곱수를 출력하면 된다.
이유) 짝수는 항상 약수/배수의 관계임
풀이2)홀수번째에 전부 1 넣고 나머지는 원래 수를 넣은 다음 값 계산
조건 만족 안 하면 짝수번째에만 1 넣은거 출력하면 된다.
'''
t = ii()
for _ in range(t):
    n = ii()
    A = lmii()
    for i in range(n):
        tmp = 1
        while tmp <= A[i]:
            tmp*=2
        print(str(tmp//2)+" ")
    print('\n')
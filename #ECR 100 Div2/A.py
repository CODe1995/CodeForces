##########################################################
import sys
input = sys.stdin.readline
def ii():return int(input())
def mii():return map(int,input().rstrip().split())
def lmii():return list(map(int,input().rstrip().split()))
##########################################################
'''
[문제]
몬스터 세 마리를 죽인다.
일반공격 6회 전체공격 1회를 반복한다.
모든 몬스터는 반드시 전체공격때만 죽일 수 있다.

[조건]
1. 세 수의 합이 9의 배수
2. 각 수가 최소한의 크기를 가져야 함
'''
t = ii()
for _ in range(t):
    a,b,c = mii()
    s = a+b+c
    k = s//9
    if s%9==0 and a>=k and b>=k and c>=k:
        print('YES')
    else:
        print('NO')
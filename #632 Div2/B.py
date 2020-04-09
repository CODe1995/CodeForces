
import sys
inp = sys.stdin

t = int(inp.readline().strip())


for i in range(t):
    N = int(inp.readline().strip())
    arr1 = list(map(int,inp.readline().split()))
    arr2 = list(map(int,inp.readline().split()))

    if sum(arr1)==sum(arr2):
        print('YES')
    else:
        if  sum(arr1)!=0 and sum(arr2)!=0:
            if sum(arr1)%sum(arr2)==0 or sum(arr2)%sum(arr1)==0:
                print('YES')
            else:
                print('NO')
        else:
            print('NO')

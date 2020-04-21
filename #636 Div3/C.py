import sys
input = sys.stdin.readline

t = int(input())
while t:
    t-=1
    n=int(input())
    arr= list(map(int,input().split()))
    minus=False
    plus=False
    for i in arr:
        if i<0:
            minus=True
        else:
            plus=True
        if minus==True and plus==True:
            break
    brk=False
    ans=[]
    i=0
    flag='plus' if arr[0]>0 else 'minus'
    if (plus==True and minus==False) or (plus==False and minus==True):
        print(max(arr))
    else:
        while i<len(arr):
            maxnum=0
            while arr[i]>0 and flag=='plus':
                maxnum=max(maxnum,arr[i])                
                i+=1          
                if i>=len(arr):break
                elif arr[i]<0:break
            
            
            if maxnum!=0:
                flag='minus'
                ans.append(maxnum)
            if i>=len(arr):break

            maxnum=-1000000001
            while arr[i]<0 and flag=='minus':        
                maxnum=max(maxnum,arr[i])                
                i+=1
                
                if i>=len(arr):break
                elif arr[i]>0:break
            if maxnum!=-1000000001:
                flag='plus'
                ans.append(maxnum)
        
        # for inans in ans:
        #     print(inans,end=' ')
        # print()
        print(sum(ans))
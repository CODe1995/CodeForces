import sys
input = sys.stdin.readline

class Tree:
    def __init__(self,me,child=None):
        self.me = me        
        if child==None:
            self.child = list()
        elif child!=None and len(self.child)>0:
            self.child = self.child.append(child)        

n,k = map(int,input().split())
for i in range(1,n+1):
    Tree(i)
while n-1:
    n-=1
    a,b = map(int,input().split())
    if a>b: a,b=b,a    
    Tree(a,b)
print(Tree)    
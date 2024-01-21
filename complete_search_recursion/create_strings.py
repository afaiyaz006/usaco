import sys
sys.setrecursionlimit(4*10**4)
counts=0
final=[]
def search(s,perm,choosen):
    if len(s)==len(perm):
        res="".join(perm)
        final.append(res)
    else:
        for i in range(0,len(s)):
          
            if not choosen[i]:
                choosen[i]=True
                perm.append(s[i])
                search(s,perm,choosen)
                choosen[i]=False
                if(len(perm)>0):
                    perm.pop()
                
                
        

if __name__=='__main__':
    s=str(input())
    perm=[]
    choosen=dict([(i,False) for i in range(0,len(s))])
    search(s,perm,choosen)
    final=list(set(final))
    print(len(final))
    final.sort()
    for i in final:
        print(i)



    

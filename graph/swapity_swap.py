from math import ceil
def rev(l,a,b):
    p1=a-1
    p2=b-1
    while(p1<p2):
        l[p1],l[p2]=l[p2],l[p1]
        p1+=1
        p2-=1
    return l

if __name__=='__main__':
    n,k=map(int,input().split())
    a1,a2=map(int,input().split())
    b1,b2=map(int,input().split())
    l=[i+1 for i in range(0,n)]
    res=[]
    res.append(l.copy())
    count=1
    while 1:
        l=rev(l,a1,a2)
        l=rev(l,b1,b2)
       
        if res[0]==l:
            break
        res.append(l.copy())
        count+=1
    r=""
    for i in res[k%count]:
        print(i)





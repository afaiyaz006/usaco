import sys


input = open("div7.in", "r").readline

print = open("div7.out", "w").write

if __name__=='__main__':
    t=int(input())
    x=[0]*(t+1)
    rems=[0]*(t+1)
    a=dict()
    c=0
    p=0
    while t:
        d=int(input())
        x[c+1]=x[c]+d
        rems[c+1]=x[c+1]%7
        if rems[c+1] not in a:
            a[rems[c+1]]=c+1
        p=max(p,max(x[c+1],x[c]))   
        t-=1
        c+=1
    

    p1=1
    p2=len(rems)-1
    c=0
    for i in range(len(x)-1,-1,-1):
        if rems[i] in a:
            c=max(c,i-a[rems[i]])
            
    print(f"{c}\n")
    
        
        

import sys


input = open("div7.in", "r").readline

print = open("div7.out", "w").write

if __name__=='__main__':
    t=int(input())
    x=[0]*(t+1)
    rems=[0]*(t+1)
    a=dict()
    c=0
    p=0
    while t:
        d=int(input())
        x[c+1]=x[c]+d
        rems[c+1]=x[c+1]%7
        if rems[c+1] not in a:
            a[rems[c+1]]=c+1
        p=max(p,max(x[c+1],x[c]))   
        t-=1
        c+=1
    

    p1=1
    p2=len(rems)-1
    c=0
    for i in range(len(x)-1,-1,-1):
        if rems[i] in a:
            c=max(c,i-a[rems[i]])
            
    print(f"{c}\n")
    
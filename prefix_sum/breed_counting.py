

import sys


input = open("bcount.in", "r").readline

print = open("bcount.out", "w").write
if __name__=='__main__':
    t,q=map(int,input().split())
    a=[0]*(t+1)
    b=[0]*(t+1)
    c=[0]*(t+1)
    for i in range(0,t):
        n=int(input())
        if n==1:
            a[i+1]=a[i]+1
            b[i+1]=b[i]
            c[i+1]=c[i]
        elif n==2:
            a[i+1]=a[i]
            b[i+1]=b[i]+1
            c[i+1]=c[i]
        else:
            a[i+1]=a[i]
            b[i+1]=b[i]
            c[i+1]=c[i]+1
    while q:
        x,y=map(int,input().split())

        print(f"{a[y]-a[x-1]} {b[y]-b[x-1]} {c[y]-c[x-1]}")
        q-=1

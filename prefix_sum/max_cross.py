import sys


input = open("maxcross.in", "r").readline

print = open("maxcross.out", "w").write
n,k,b=map(int,input().split())
a=[0 for i in range(n)]
while b:
    x=int(input())
    a[x-1]=1
    b-=1
s=[0]
for i in a:
    s.append(s[-1]+i)

res=n
for i in range(1,len(s)):
    if i+k-1<len(s):
        res=min(res,s[i+k-1]-s[i-1])

print(str(res))
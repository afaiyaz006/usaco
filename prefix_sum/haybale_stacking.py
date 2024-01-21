
if __name__=='__main__':
    n,k=map(int,input().split())
    d=[0 for i in range(n+1)]
    s=[0 for i in range(n+1)]
    for i in range(k):
        a,b=map(int,input().split())
        
        d[a]+=1
        if b+1<=n:
            d[b+1]-=1
    for i in range(1,len(d)):
        s[i]=s[i-1]+d[i]
   
    s=s[1:]
    s.sort()

    print(f"{s[(n//2)]}")


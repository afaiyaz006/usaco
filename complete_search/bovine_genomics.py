
import sys
sys.stdin=open("cownomics.in","r")
sys.stdout=open("cownomics.out","w")



if __name__=='__main__':
    n,m=map(int,input().split())
    spotty=[]
    plain=[]
    t=n
    while t:
        data=list(input())
        spotty.append(data)
        t-=1
    t=n
    while t:
        data=list(input())
        plain.append(data)
        t-=1

    counter=0
    for i in range(0,m):
        spotty_seq=set()
        plain_seq=set()
        for j in range(0,n):
            spotty_seq.add(spotty[j][i])
            plain_seq.add(plain[j][i])
        
        if len(spotty_seq&plain_seq)==0:
            counter+=1
    print(counter)

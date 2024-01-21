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
    for i in range(0,len(spotty)):
        for j in range(0,len(spotty)):
            for k in range(j+1,len(spotty)-2,2):
                a=[j,k,k+1]
                print(a)

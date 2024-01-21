import sys
sys.stdin=open("square.in","r")
sys.stdout=open("square.out","w")

if __name__=='__main__':
    x1,y1,x2,y2=map(int,input().split())
    x3,y3,x4,y4=map(int,input().split())
    dist_A=max([x1,x2,x3,x4])-min([x1,x2,x3,x4])
    dist_B=max([y1,y2,y3,y4])-min([y1,y2,y3,y4])
    res=max(dist_A,dist_B)
    res=int(res)
    res*=res
    print(res)


import sys
sys.stdin=open("race.in","r")
sys.stdout=open("race.out","w")
if __name__=='__main__':
    k,n=map(int,input().split())
    for i in range(0,n):
        x=int(input())
        speed=1
        distance=0
        time=0
        while distance<k:
            if distance+speed+((speed*(speed-1))//2)>=k and speed>x:
                speed-=1
            else:
                distance+=speed
                speed+=1
                time+=1
        print(time)
                


import sys
sys.stdin=open("gymnastics.in","r")
sys.stdout=open("gymnastics.out","w")

if __name__=='__main__':
    n,t=map(int,input().split())
    data=[]
    while n:
        a=[int(_) for _ in input().split()]
        data.append(a)
        n-=1
    original=data[0]
    result=[]
    for i in range(0,len(original)-1):
        for j in range(i+1,len(original)):
            pair_1=original[i]
            pair_2=original[j]
            #print(pair_1,pair_2)
            counter=0
            for x in range(0,len(data)):
                p1=-1
                p2=-1
                for y in range(0,len(data[x])):
                    if pair_1==data[x][y]:
                        p1=y
                    elif pair_2==data[x][y]:
                        p2=y
                    elif p1!=-1 and p2!=-1:
                        break

                    
                if p1<p2 and p1!=-1 and p2!=-1:
                    counter+=1
                else:
                    break
                
            
            if counter==len(data):
                result.append((pair_1,pair_2))

    print(len(result))
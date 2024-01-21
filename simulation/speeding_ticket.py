
import sys
sys.stdin=open("speeding_ticket.in","r")
sys.stdout=open("speeding_ticket.out","w")

if __name__=='__main__':
    n,m=map(int,input().split())
    police=[]
    bessy=[]
    police_dict=dict()
    bessy_dict=dict()
    prev=0
    
    for i in range(0,n):
        x,y=map(int,input().split())
        police.append((prev+x,y))
        prev=prev+x
    
    prev=0
    
    for i in range(0,m):
        x,y=map(int,input().split())
        bessy.append((prev+x,y))
        prev=prev+x

    pointer_1=0
    pointer_2=0
    for i in range(0,101):
        if pointer_1<n:
            if i>police[pointer_1][0]:
                pointer_1+=1
                if(pointer_1<n):
                    police_dict[i]=police[pointer_1][1]
                else:
                    police_dict[i]=police[pointer_1-1][1]
            else:
                police_dict[i]=police[pointer_1][1]
        else:
            police_dict[i]=police[pointer_1-1][1]
    
    for i in range(0,101):
        if pointer_2<m:
            if i>bessy[pointer_2][0]:
                pointer_2+=1
                if pointer_2<m:
                    bessy_dict[i]=bessy[pointer_2][1]
                else:
                    bessy_dict[i]=bessy[pointer_2-1][1]
            else:
                bessy_dict[i]=bessy[pointer_2][1]
        else:
            bessy_dict[i]=bessy[pointer_2-1][1]
    
    res=0
    for i in range(0,101):
        
        if bessy_dict[i]>police_dict[i]:
        
            res=max(res,bessy_dict[i]-police_dict[i])
    print(res)
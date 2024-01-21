import sys
sys.stdin=open("backforth.in","r")
sys.stdout=open("backforth.out","w")
result=set()
def solve(t_1,t_2,taken_1,taken_2,mc_1,mc_2,depth):
    if depth>3:
        result.add(mc_1)
    else:
    
        if depth%2==0:
            for i in range(0,len(t_1)):
                if not taken_1[i]:
                    value=t_1[i]
                    taken_1[i]=True
                    solve(t_1,t_2,taken_1,taken_2,mc_1-value,mc_2+value,depth+1)
                    taken_1[i]=False
            for i in range(0,len(t_2)):
                if taken_2[i]:
                    value=t_2[i]
                    taken_2[i]=False
                    solve(t_1,t_2,taken_1,taken_2,mc_1-value,mc_2+value,depth+1)
                    taken_2[i]=True 
        else:
            for i in range(0,len(t_2)):
                if not taken_2[i]:
                    value=t_2[i]
                    taken_2[i]=True
                    solve(t_1,t_2,taken_1,taken_2,mc_1+value,mc_2-value,depth+1)
                    taken_2[i]=False
            for i in range(0,len(t_1)):
                if taken_1[i]:
                    value=t_1[i]
                    taken_1[i]=False
                    solve(t_1,t_2,taken_1,taken_2,mc_1+value,mc_2-value,depth+1)      
                    taken_1[i]=True
        
            
                
        

if __name__=='__main__':
    storage_closet_1=list(map(int,input().split(' ')))
    storage_closet_2=list(map(int,input().split(' ')))
    milk_tank_1=1000
    milk_tank_2=1000
    temp_1=[]
    temp_2=[]
    taken_1=[False for i in range(0,len(storage_closet_1))]
    taken_2=[False for i in range(0,len(storage_closet_2))]

    solve(storage_closet_1,storage_closet_2,taken_1,taken_2,milk_tank_1,milk_tank_2,0)
    print(len(result))

    
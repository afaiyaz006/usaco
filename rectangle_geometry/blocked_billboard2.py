import sys
sys.stdin=open("billboard.in","r")
sys.stdout=open("billboard.out","w")
def intersect(s1,s2):
    bl_ax,bl_ay,tr_ax,tr_ay=s1[0],s1[1],s1[2],s1[3]
    bl_bx,bl_by,tr_bx,tr_by=s2[0],s2[1],s2[2],s2[3]

    return (min(tr_ax,tr_bx)-max(bl_ax,bl_bx))*(min(tr_ay,tr_by)-max(bl_ay,bl_by))

if __name__=='__main__':
    x1,y1,x2,y2=map(int,input().split())
    x3,y3,x4,y4=map(int,input().split())
    s1=lawn_mower_billboard=(x1,y1,x2,y2)
    s2=cowfeed_billboard=(x3,y3,x4,y4)
    intersecting_area=intersect(lawn_mower_billboard,cowfeed_billboard)
    area_of_lawnmower_billboard=abs(x2-x1)*abs(y2-y1)
    area_of_cowfeed_billboard=abs(x3-x4)*abs(y3-y4)
    if intersecting_area<=0:
        print(area_of_lawnmower_billboard)
    elif intersecting_area==area_of_lawnmower_billboard:
        print(0)
    else:
        x5,y5,x6,y6=max(s1[0],s2[0]),max(s1[1],s2[1]),min(s1[2],s2[2]),min(s1[3],s2[3])
        if  (x5==x1 and  y1==y5 and y2==y6) or (x2==x6 and y1==y5 and y2==y6):
            print(area_of_lawnmower_billboard-intersecting_area)
        elif (y5==y1 and x1==x5 and x2==x6) or (y6==y2 and x1==x5 and x2==x6):
            print(area_of_lawnmower_billboard-intersecting_area)
            
        
        else:
            print(area_of_lawnmower_billboard)

        
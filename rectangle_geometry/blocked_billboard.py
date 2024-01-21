import sys
sys.stdin=open("billboard.in","r")
sys.stdout=open("billboard.out","w")
def inter_area(p1, p2) -> int:
	bl_a_x, bl_a_y, tr_a_x, tr_a_y = p1[0], p1[1], p1[2], p1[3]
	bl_b_x, bl_b_y, tr_b_x, tr_b_y = p2[0], p2[1], p2[2], p2[3]
	
	return (
		(min(tr_a_x, tr_b_x) - max(bl_a_x, bl_b_x))
		* (min(tr_a_y, tr_b_y) - max(bl_a_y, bl_b_y))
	)

if __name__=='__main__':

    x1,y1,x2,y2=map(int,input().split())
    x3,y3,x4,y4=map(int,input().split())
    x5,y5,x6,y6=map(int,input().split())

    area_1=abs(x1-x2)*abs(y1-y2)
    area_2=abs(x3-x4)*abs(y3-y4)
    
    p1=(x1,y1,x2,y2)
    p2=(x3,y3,x4,y4)
    p3=(x5,y5,x6,y6)

    res=min(0,area_1-inter_area(p1,p3))
    res+=min(0,area_2-inter_area(p2,p3))
    print(res)


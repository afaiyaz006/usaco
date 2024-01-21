

def inter_area(p1, p2) -> int:
    bl_a_x, bl_a_y, tr_a_x, tr_a_y = p1[0], p1[1], p1[2], p1[3]
    bl_b_x, bl_b_y, tr_b_x, tr_b_y = p2[0], p2[1], p2[2], p2[3]
    height=min(tr_a_x,tr_b_x)-max(bl_a_x,bl_b_x)
    width=min(tr_a_y,tr_b_y)-max(bl_a_y,bl_b_y)
    if height<0 or width<0:
        return -1
    else:
        return height*width

if __name__ == '__main__':
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    x5, y5, x6, y6 = map(int, input().split())
    ls1 = (x1, y1, x2, y2)
    ls2 = (x3, y3, x4, y4)
    ls3 = (x5, y5, x6, y6)
    area_0 = abs(x1-x2)*abs(y1-y2)
    area_1 = inter_area(ls1, ls2)
    area_2 = inter_area(ls1, ls3)
    black_intersect = inter_area(ls2, ls3)
    total_intersect = 0
    if area_1 >= 0:
        total_intersect += area_1
    if area_2 >= 0:
        total_intersect += area_2
    if black_intersect >= 0:
        ls4 = (max(x3, x5), max(y3, y5), min(x4, x6), min(y4, y6))
        common_intersect = inter_area(ls4, ls1)

        if common_intersect >= 0:
            total_intersect -= common_intersect

  

    area_0 -= total_intersect
    
    if area_0 > 0:
        print("YES")
    else:
        print("NO")

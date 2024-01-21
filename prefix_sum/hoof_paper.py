

if __name__=='__main__':
    t=int(input())
    z=[]
    h=[0]
    p=[0]
    s=[0]
    co=0
    res="*"
    label_p=[]
    label_h=[]
    label_s=[]
    
    
    while t:
        c=input()
        res+=c
        uph,ups,upp=0,0,0
        if c=='H':
            uph=1
        if c=='S':
            ups=1
        if c=='P':
            upp=1
        h.append(h[-1]+uph)
        s.append(s[-1]+ups)
        p.append(p[-1]+upp)

        t-=1
    g_c=0
    g_c_1=0
    g_c_2=0
    for i in range(len(h)):
        g_c_1=max(h[-1]-h[i],p[-1]-p[i],s[-1]-s[i])
        g_c_2=max(p[i],h[i],s[i])
        g_c=max(g_c,g_c_1+g_c_2)
    print(f"{g_c}")
    
   
   
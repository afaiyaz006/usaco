a=[False for i in range(3)]
b=[1,2,3]
res=[]
def f(res):
    if len(res)==3:
        print(res)
        
    else:
        for i in range(0,3):
            if a[i]==False:
                a[i]=True
                res.append(i)
                f(res)
                res.pop()
                a[i]=False


f(res)
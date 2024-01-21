
def f(n):
    if n==0:
        return 
    c+=10
    print(c)
    a[n]=3
    a.append(3)
    print(a)
    f(n-1)


if __name__=='__main__':
    a=[1,2,3,4,5,6]
    n=3
    c=0
    f(n)
    print(a)
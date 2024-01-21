
def search(i,s1,s2):
    if i==n:
        return abs(s1-s2)
    else:
        return min(search(i+1,s1+a[i],s2),search(i+1,s1,s2+a[i]))
    
if __name__=='__main__':
    n=int(input())
    a=list(map(int,input().split()))
    print(search(0,0,0))


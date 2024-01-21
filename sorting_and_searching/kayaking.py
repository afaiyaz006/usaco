if __name__=='__main__':
    n=int(input())
    numbers=list(map(int,input().split()))
    numbers.sort()
    res=1000000
    for i in range(0,len(numbers)):
        for j in range(0,len(numbers)):
            if i!=j:
                new_one=[numbers[x] for x in range(0,len(numbers)) if x!=j and x!=i]
               
                diff=0
                for k in range(0,len(new_one),2):
                    diff+=new_one[k+1]-new_one[k]
               
                res=min(diff,res)
    print(res)


    
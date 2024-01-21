import sys
sys.stdin=open("whereami.in","r")
sys.stdout=open("whereami.out","w")
if __name__=='__main__':
    n=int(input())
    s=input()
    check=set()
    res=n
    for i in range(0,len(s)):
        check=set()

        for j in range(0,len(s)-i):
            string=s[j:j+i+1]
          
            if string in check:
                check.clear()
                break
            else:
                check.add(string)
        if len(check)>0:
            res=min(res,i+1)
    print(res)    

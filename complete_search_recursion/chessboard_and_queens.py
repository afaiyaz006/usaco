n=8
count=0
def search(col:int):
    global n
    if(col==n):
        global count
        count+=1
        return
    else:
        for row in range(0,n):
            if column[row]==1 or diag1[row+col]==1 or diag2[row-col+n-1]==1 or grid[row][col]=='*':
                continue
          
            column[row]=1
            diag1[row+col]=1
            diag2[row-col+n-1]=1
            search(col+1)
            column[row]=0
            diag1[row+col]=0
            diag2[row-col+n-1]=0
            
    
if __name__=='__main__':
    grid=[str(input()) for i in range(n)]
    reserved=[]
    column=[0 for i in range(0,8)]
    diag1=[0 for i in range(0,17)]
    diag2=[0 for i in range(0,17)]

    search(0)
    print(count)
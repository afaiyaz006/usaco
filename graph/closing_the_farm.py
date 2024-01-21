from collections import deque
import sys
sys.stdin = open("closing.in", "r")
sys.stdout = open("closing.out", "w")
def bfs(graph,
        start_node,
        ):
    visited=[False]*(n+1)
    q=deque()
    q.append(start_node)
    count_=0
    visited[start_node]=True
    while q:
        node=q.popleft()
        
        for u in graph[node]:
            if not visited[u] and open[u]:
                visited[u]=True
                count_+=1
                q.append(u)
                
    
    return count_+1

    
if __name__=='__main__':
    n,m=map(int,input().split())
    graph=[[] for _ in range(n+1)]
    for i in range(m):
        i,j=map(int,input().split())
        graph[i].append(j)
        graph[j].append(i)
    
    seq=[]
    for i in range(n):
        x=int(input())
        seq.append(x)



    start_node=seq[-1]
    open=[True]*(n+1)
    counts=bfs(graph,start_node)
    if counts==n:
        print("YES")
    else:
        print("NO")
    c_n=n

    for num in seq:
        if start_node==num:
            break
        c_n=c_n-1
        open[num]=False
        count=bfs(graph,start_node)
        if count==c_n:
            print("YES")
        else:
            print("NO")
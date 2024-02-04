
import sys
from collections import deque

sys.stdin = open("fence.in", "r")
sys.stdout = open("fence.out", "w")
# find smallest connected component
# take the min(x1..xn),min(y1..yn) and max(y1...yn),max(x1...xn)
# thus find the perimeter
def bfs(graph,
        start_node,
        visited,
        cow_pos
        ):
    q=deque()
    q.append(start_node)
    x1=cow_pos[start_node-1][0]
    y1=cow_pos[start_node-1][1]
    x2=cow_pos[start_node-1][0]
    y2=cow_pos[start_node-1][1]
    
    visited[start_node]=True
    while q:
        node=q.popleft()
            
        for u in graph[node]:
            if not visited[u]:
                visited[u]=True
                x1=min(x1,cow_pos[u-1][0])
                y1=min(y1,cow_pos[u-1][1])
                x2=max(x2,cow_pos[u-1][0])
                y2=max(y2,cow_pos[u-1][1])
                q.append(u)
                
    
    return 2*(x2-x1)+2*(y2-y1)


if __name__=='__main__':
    n,m=map(int,input().split())
    cow_pos=[]
    graph=[]
   
    
    for i in range(n):
        x,y=map(int,input().split())
        cow_pos.append((x,y))

    graph=[[] for i in range(n+1)]
    for i in range(m):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    visited=[False]*(n+1)
    c=1e10
    for i in range(n):
        if not visited[i+1]:
            
            perimeter=bfs(graph,i+1,visited,cow_pos)
            if perimeter!=0:
                c=min(c,perimeter)
    print(c)
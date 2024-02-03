from math import sqrt
from collections import deque
def bfs(graph,
        start_node,
        ):
    visited=[False]*(len(graph))
    q=deque()
    q.append(start_node)
    count_=0
    visited[start_node]=True
    while q:
        node=q.popleft()
        
        for u in graph[node]:
            if not visited[u]:
                visited[u]=True
                count_+=1
                q.append(u)
                
    
    return count_+1

if __name__=='__main__':
    t=int(input())
    gorus=[]
    graph={

    }
    while t:
        x,y,p=map(int,input().split())
        gorus.append((x,y,p))
        t-=1

    # graph banai
    for i in range(0,len(gorus)):
        source=gorus[i]
        graph[i]=[]
        for j in range(0,len(gorus)):
            if i!=j:
                x1=gorus[i][0]
                y1=gorus[i][1]
                x2=gorus[j][0]
                y2=gorus[j][1]
                dis=sqrt((x1-x2)**2+(y1-y2)**2)
                if dis<=gorus[i][2]:
                    graph[i].append(j)
    #bfa lagai
    c=0
    for i in range(0,len(gorus)):
        c=max(c,bfs(graph,i))
    print(c)
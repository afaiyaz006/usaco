from collections import deque
q=deque()
def bfs(graph,visited,source=None):
    if not source:
        source=list(graph.keys())[0]
    distance=dict()
    q.append(source)
    visited[source]=True
    distance[source]=0
    while len(q)>0:
        source=q.pop()
        
        for node in list(graph[source]):
            if  node not in visited:
                distance[node]=distance[source]+1
                visited[node]=True
                q.append(node)
    print(distance,visited)



if __name__=='__main__':
    graph=dict()
    dis=dict()
    nodes=set()
    visited=dict()
    m=int(input("Enter number of edges: "))
    for i in range(0,m):
        x,y=map(int,input().split())
        if x in graph:
            graph[x].add(y)
        else:
            graph[x]=set([y])
        if y in graph:
            graph[y].add(x)
        else:
            graph[y]=set([x])
        nodes.add(x)
        nodes.add(y)
    
    print(graph)
    source=list(graph.keys())[0]
    
    bfs(source,graph,visited)

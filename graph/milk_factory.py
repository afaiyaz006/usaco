from collections import deque
read = open("milk_factory.in", "r").readline
write = open("milk_factory.out", "w").write
def bfs(graph,source):
    q=deque()
    visited=[False for i in range(0,101)]
    q.append(source)
   
    last_node=source
    while q:
        source=q.pop()
        last_node=source
        for node in graph[source]:
            if not visited[node]:
                visited[node]=True
                q.append(node)
    return last_node
    
if __name__=='__main__':
    n=int(read())
    graph=[[] for i in range(0,101)]
    nodes=set()
    for i in range(0,n-1):
        u,v=map(int, read().split())
        graph[u].append(v)
        nodes.add(u)
        nodes.add(v)
    prev=0
    nodes=list(nodes)
    for node in nodes:
        last_node=bfs(graph,node)
        if prev==0:
            prev=last_node
        elif prev!=last_node:
            prev=-1
            break
    write(str(prev) + "\n")
    
    
        
        
        
    
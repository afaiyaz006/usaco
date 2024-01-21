
def dfs(source,graph):
    
    visited[source]=True
    print(source)
    for node in list(graph[source]):
        if node not in visited:    
            dfs(node,graph)

if __name__=='__main__':
    graph=dict()
    nodes=set()
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
    visited=dict()
    print(graph)
    dfs(list(graph.keys())[0],graph)

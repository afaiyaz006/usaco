from collections import deque


if __name__=='__main__':
    n=int(input())
    graph=dict()
    for i in range(0,n-1):
        u,v=map(int,input().split())
        if u not in graph:
            graph[u]=list()
        if v not in graph:
            graph[v]=list()
        graph[u].append(v)
        graph[v].append(u)
        
    colors=3
    extra=0
    for node in list(graph.keys()):
        adjancents=len(list(graph[node]))
        if adjancents>2:
            extra=max(extra,adjancents-2)
    
    
    print(colors+extra)
        
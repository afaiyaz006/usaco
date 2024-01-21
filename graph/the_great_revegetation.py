def color_short(graph,nodes):
    for node in range(1,nodes+1):
        pallete=[0,0,0,0,0]
        for adj in graph[node]:
            pallete[color[adj]]=1
        for i in range(1,len(pallete)+1):
            if pallete[i]!=1:
                color[node]=i
                break
    res=""
    for cl in color[1:]:
        res+=str(cl)
    print(res)

if __name__=='__main__':
    n,m=map(int,input().split())
    graph=[[] for i in range(0,n+1)]
    nodes=n
    color=[0 for i in range(0,n+1)]
    for i in range(0,m):
        u,v=map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)

    color_short(graph,nodes)
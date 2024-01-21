from collections import deque
def check_bipirate(graph):
    dis=dict()
    colors=dict()
    source=list(graph.keys())[0]
    q=deque()
    q.append(source)
    dis[source]=0
    flag=True
    while len(q)>0:
        source=q.pop()
        if dis[source]&1:
            colors[source]='RED'
        else:
            colors[source]='GREEN'
        for node in list(graph[source]):
            if node not in dis:
                dis[node]=dis[source]+1
                q.append(node)
            if node in colors and colors[node]==colors[source]:
                flag=False
                break
        
    if flag:
        print("Bipirateness Possible")
        print(colors)
    else:
        print("Is not Bipirate")           
    
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
    check_bipirate(graph)
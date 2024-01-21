import bfs

if __name__=='__main__':
    graph={
        1:set([2,3]),
        5:set([6,7]),
        2:set([1]),
        3:set([1]),
        6:set([5]),
        7:set([5])
    }
    nodes=[1,2,3,5,6,7]
    visited=dict()
    graphs=0
    for node in nodes:
       if node not in visited:
            graphs+=1
            bfs.bfs(graph,visited,node)
    print(graphs)
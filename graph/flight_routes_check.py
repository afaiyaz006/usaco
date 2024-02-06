from collections import deque
import sys
# need to use this
input = sys.stdin.readline
print=sys.stdout.write
# used Kosaraju’s Algorithm
sys.setrecursionlimit(20000000)
def dfs(graph,node):
 
    visited[node]=True
    priority.append(node)
    for neighbour in graph[node]:
        if not visited[neighbour]:
            dfs(graph,neighbour)
    
 
if __name__=='__main__':
    n,m=map(int,input().split())
    graph=[[] for i in range(n+1)]
    transposed_graph=[[] for i in range(n+1)]
    for i in range(m):
        a,b=map(int,input().split())
        graph[a].append(b)
        transposed_graph[b].append(a)
    
    visited=[False]*(n+1)
    priority=[]
    dfs(graph,1)  # dfs 1
    count=0
    strongly_connected=False
    weakly_connected=True
    node_set=[]
    for i in range(1,n+1):# checking if the graph is weakly connected atleast if not found a solution
        if visited[i]==False:
            print(f"NO\n")
            print(f"1 {i}\n")
            weakly_connected=False
            break
    
 
    if weakly_connected:
       
        visited=[False]*(n+1)
   
 
        for node in priority:
            if not visited[node]:
                node_set.append(node)# finding new component and appending them
                dfs(transposed_graph,node)
                count+=1
            if count>1:# dont need to check for more than 2 components 
                strongly_connected=True
                break
        if count==1:
            print("YES\n")
        else:
            print("NO\n")
            print(f"{node_set[1]} {node_set[0]}")
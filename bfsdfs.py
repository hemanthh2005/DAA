from test.dtracedata.gc import start


def dfs(graph,start,visited=None):
    if visited is None:
        visited=set()
    print(start,end=" ")
    visited.add(start)

    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph,neighbour,visited)

from collections import deque
def bfs(graph,start):
    visited=set()
    queue=deque([start])
    while queue:
        node=queue.popleft()
        if node not in visited:
            print(node,end=" ")
            visited.add(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)

graph={
    'A':['C','D','E'],
    'B':['E','F'],
    'C':['D','F'],
    'D':['A','C'],
    'E':['A','B','F'],
    'F':['E','F']
}
print("DFS traversal")
dfs(graph,'A')

print("\n BFS traversal")
bfs(graph,'A')
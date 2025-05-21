def all_pair_short(dist,n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j]=min(dist[i][j],(dist[i][k]+dist[k][j]))

def transit_closure(reach,n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                reach[i][j]=(reach[i][j]) or (reach[i][k] and reach[k][j])

graph=[[0,100,3,100],[2,0,100,100],[100,7,0,1],[6,100,100,0]]
n=4
all_pair_short(graph,n)
print("all pair shortest path")
for i in range(n):
    print(graph[i])

graph=[[0,1,0,0],[0,0,0,1],[0,0,0,0],[1,0,1,0]]
n=4
transit_closure(graph,n)
print("\n transitive closure")
for i in range(n):
    print(graph[i])
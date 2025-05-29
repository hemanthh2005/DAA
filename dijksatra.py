def near_vertex(d, vt):
    min_dist = 999
    v = -1
    for i in range(len(d)):
        if i not in vt:
            if d[i] < min_dist:
                min_dist = d[i]
                v = i
    return v

def path(v, pv, a):
    if pv[v] != -1:
        a.append(pv[v])
        path(pv[v], pv, a)

def print_paths(d, pv):
    for i in range(len(d)):
        print("Path to vertex:", i)
        a = []
        path(i, pv, a)
        a.reverse()
        a.append(i)
        print(a)

def dijkstra(graph):
    n = len(graph)
    d = [999] * n         # Distance array initialized to "infinity"
    pv = [-1] * n         # Parent array
    vt = []               # Visited list

    s = 0                 # Start from source vertex 0
    d[s] = 0              # Distance to source is 0

    for _ in range(n):
        v = near_vertex(d, vt)
        if v == -1:
            break
        vt.append(v)

        adj_vertex = graph[v]
        for val in adj_vertex:
            node = val[0]
            weight = val[1]
            if node not in vt:
                if d[v] + weight < d[node]:
                    d[node] = d[v] + weight
                    pv[node] = v

    print_paths(d, pv)

# Driver Code
graph = {
    0: [[3, 7]],
    1: [[2, 4]],
    2: [[4, 6]],
    3: [[1, 2], [2, 5]],
    4: [[3, 4]]
}

dijkstra(graph)

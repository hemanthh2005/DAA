def find_set(all_set, key):
    for i in range(len(all_set)):
        if key in all_set[i]:
            return i

def kruskal(edge, vert):
    edge.sort(key=lambda x: x[2])  # Sort edges by weight
    all_set = []

    # Initially each vertex is in its own set
    for k in vert:
        a = [k]
        all_set.append(a)

    st_edge = []  # To store the edges of the MST
    i = 0
    ct = 0
    n = len(vert)

    while ct < n - 1:
        x, y, w = edge[i]
        s1 = find_set(all_set, x)
        s2 = find_set(all_set, y)

        if s1 != s2:
            st_edge.append([x, y, w])
            all_set[s1] = all_set[s1] + all_set[s2]
            del all_set[s2]
            ct += 1

        i += 1

    return st_edge

# Driver code
edge = [
    ['a', 'b', 5], ['b', 'd', 6], ['c', 'd', 4],
    ['a', 'c', 7], ['a', 'e', 2], ['b', 'e', 3],
    ['d', 'e', 5], ['c', 'e', 4]
]

vert = ['a', 'b', 'c', 'd', 'e']

# Call the Kruskal function
mst = kruskal(edge, vert)

# Print the resulting Minimum Spanning Tree
print("Edges in MST:")
print(mst)
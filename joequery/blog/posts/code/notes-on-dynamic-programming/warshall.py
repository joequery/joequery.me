def warshall(A, n):
    R = []
    R.insert(0, A)
    k = 1
    while k <= n:
        R.insert(k, [])
        i = 0
        while i <= n-1:
            R[k].insert(i, [])
            j = 0
            while j <= n-1:
                hasPath = R[k-1][i][j] or (R[k-1][i][k-1] and R[k-1][k-1][j])
                R[k][i].insert(j, int(hasPath))
                j += 1
            i += 1
        k += 1
    return R[n]
                


# Adjacency matrix of the graph used through the examples in the notes.
adj = [
    [0,0,1,0],
    [1,0,0,1],
    [0,0,0,0],
    [0,1,0,0],
]

print(warshall(adj, 4))

import sys
import copy
INF = sys.maxint # use max_int as 'infinity'

def floyd(W, n):
    D = copy.deepcopy(W)
    k = 0
    while k < n:
        i = 0
        while i < n:
            j = 0
            while j < n:
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
                j += 1
            i += 1
        k += 1
    return D
                


# weight matrix of the graph used through the examples in the notes.
W = [
    [0,INF,3,INF],
    [2,0,INF,INF],
    [INF,7,0,1],
    [6,INF,INF,0],
]

print(floyd(W, 4))

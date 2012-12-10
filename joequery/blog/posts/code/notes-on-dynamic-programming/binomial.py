def binomial(n,k):
    C = []
    i = 0
    x = 0
    while i <= n:
        j = 0
        C.insert(i, [])
        while j <= min(i,k):
            if j == 0 or j == i:
                C[i].insert(j, 1)
            else:
                C[i].insert(j, C[i-1][j-1] + C[i-1][j])
            j += 1
            x += 1
        i += 1
    print("Number of additions: %d" % x)
    return C[n][k]

print(binomial(5,2)) # 10 

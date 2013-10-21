def euclid(a, b):
    '''
    Find the gcd of a and b (with a >= b)
    '''
    q,r = divmod(a,b)
    while r != 0:
        a = b
        b = r
        q,r = divmod(a,b)
    return b

print(euclid(25, 120))
print(euclid(18, 81))

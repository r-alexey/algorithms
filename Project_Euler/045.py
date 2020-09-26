def triangle(n):
    return int(n*(n+1)/2)

# --------

def is_pentagonal(n):
''' p = n(3n-1)/2
    2p = 3n^2 - n
    3n^2 - n - 2p = 0
    D = (-1)^2 - 4 * 3 * (-2p)
    D = 1 + 24p
    x1 = (1 + D^0.5) / 6
    x2 = (1 - D^0.5) / 6 '''
    D = 1 + 24*n

    x1 = (1 + D**0.5) / 6
    if x1 > 0:
        if x1 % 1 == 0:
            return True

    x2 = (1 - D**0.5) / 6
    if x2 > 0:
        if x2 % 1 == 0:
            return True

    return False

# --------

def is_hexagonal(n):
''' h = n(2n-1)
    h = 2n^2 - n
    2n^2 - n - h = 0
    D = (-1)^2 - 4 * 2 * (-h)
    D = 1 + 8h
    x1 = (1 + D^0.5) / 4
    x2 = (1 - D^0.5) / 4 '''
    D = 1 + 8*n

    x1 = (1 + D**0.5) / 4
    if x1 > 0:
        if x1 % 1 == 0:
            return True

    x2 = (1 - D**0.5) / 4
    if x2 > 0:
        if x2 % 1 == 0:
            return True

    return False

# --------

n = 285

while True:
    n += 1
    t = triangle(n)
    
    if is_pentagonal(t) and is_hexagonal(t):
        print(t)
        break

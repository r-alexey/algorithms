def euclid_alg(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return (a + b)


y = 1000001
max_x = 1
max_y = 1000000

while y > 7:
    
    y -= 1
    x = int(y * 3/7)

    while x > 3:
        if euclid_alg(x, y) == 1:
            if x/y > max_x/max_y:
                max_x = x
                max_y = y
            break
        x -= 1

print(max_x)

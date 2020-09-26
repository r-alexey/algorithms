def euclid_alg(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return (a + b)

lst = []

for m in range(2, 500):

    for n in range(1, m):

        if euclid_alg(m, n) != 1:
            continue
        elif (m - n) % 2 == 0:
            continue
        
        else:
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2
            
            for i in range(1, 500):
                p = (a+b+c)*i
                if p > 1000:
                    break
                lst.append(p)

unic = set(lst)
max_qty = 0
max_item = 0
        
for item in unic:
    if max_qty < lst.count(item):
        max_qty = lst.count(item)
        max_item = item

        
print (max_item)

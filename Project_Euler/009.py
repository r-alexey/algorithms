#______________FIRST_WAY______________#

ans = 0

for a in range(1, 333):
    rest = 1000 - a


    if rest % 2 == 0:
        max_b = int(rest / 2 - 1)
    else:
        max_b = int((rest - 1) / 2)


    for b in range(a + 1, max_b + 1):
        c = 1000 - a - b
        if (a**2 + b**2 == c**2):
            ans = a * b * c
            break


    if ans != 0:
        break


print(ans)



#_____________SECOND_WAY_____________#
# Theory:
# If   a > b > c   and   a**2 + b**2 = c**2
# Then:
# m > n
# a = m**2 - n**2
# b = 2 * m * n
# c = m**2 + n**2
# -----
# a + b + c = 1000   =>
# m**2 - n**2 + 2 * m * n + m**2 + n**2 = 1000
# 2 * m**2 + 2 * m * n = 1000
# 2 *( m**2 + m*n ) = 1000
# m**2 + m*n = 500


n = 1
m = 2

while True:
    summ = m**2 + m * n

    if summ < 500:
        m += 1
    elif summ > 500:
        n += 1
        m = n + 1
    else:
        break


a = m**2 - n**2
b = 2 * m * n
c = m**2 + n**2


print (a * b * c)
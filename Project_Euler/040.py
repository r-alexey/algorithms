num = 0
leng = 0
d = 1
ans = 1

while True:
    num += 1
    leng += len(str(num))

    if leng > d:
        leng -= len(str(num))
        for item in str(num):
            leng += 1
            if leng == d:
                ans *= int(item)
                d *= 10

    elif leng == d:
        ans *= int(str(num)[-1])
        d *= 10

    if d > 1000000:
        break

print(ans)

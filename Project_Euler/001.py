#______________FIRST_WAY______________#
total = 0

for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        total += i

print(total)


#_____________SECOND_WAY_____________#
total = 0

for i in range(1, 334):
    total += 3 * i
for i in range(1, 200, 3):
    total += 5 * i
for i in range(2, 200, 3):
    total += 5 * i

print(total)

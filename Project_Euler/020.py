number = 1
for i in range(1, 101):
    number *= i

number = str(number)
total = 0
for i in number:
    total += int(i)

print(total)

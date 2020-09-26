number = 600851475143
divider = 2
largest = 0

while divider <= number:
    if number % divider != 0:
        divider += 1
        continue
    else:
        number = number / divider
        if divider > largest:
            largest = divider
        divider = 2

print (largest)

array = [i for i in range(150000)]
array [1] = 0
qty = 0


for number in array:
    if number == 0:
        continue
    else:
        qty += 1
        if qty == 10001:
            break
        for zero_number in array[number * 2 :: number]:
            array[zero_number] = 0


if qty == 10001:
    print (number)
else:
    print('10 001st prime number out of range')

largest=0
array = [i for i in range(100, 1000)]

for i in range(len(array)):
    for j in range(i, len(array)):
        num = str(array[i] * array[j])
        if num == num[::-1]:
            if int(num) > largest:
                largest = int(num)

print (largest)

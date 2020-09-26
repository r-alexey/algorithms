total = 0

for i in range(2, 1000000):
    summ = 0
    num = str(i)
    
    for j in num:
        summ += int(j)**5
        
    if int(num) == summ:
        total += summ


print(total)

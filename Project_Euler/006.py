squared_summ = 0
summ_squared_num = 0


for i in range(1, 101):
    squared_summ += i
    summ_squared_num += i ** 2


squared_summ **= 2
ans = squared_summ - summ_squared_num


print(ans)

def prime_factors(number):
    dividers_list = []
    divider = 2
    while number != 1:
        if number % divider != 0:
            divider += 1
            continue
        else:
            dividers_list.append(divider)
            number /= divider
    return(dividers_list)


result = {1: 1}

for i in range(2, 21):
    dividers_list = prime_factors(i)
    for j in dividers_list:
        if result.get(j):
            if result[j] < dividers_list.count(j):
                result.update({j: dividers_list.count(j)})
        else:
            result.update({j: dividers_list.count(j)})

ans = 1

for i in result:
    ans *= i**result[i]

print(ans)

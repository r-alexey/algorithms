def is_palindromic(num):

    num = str(num)
    leng = len(num)
    iterations = leng // 2
    ans = True
    
    for i in range(iterations):
        if num[i] != num[-(i+1)]:
            ans = False
            break

    return ans

total = 0
for number in range(1, 1000001):
    if is_palindromic(number):
        bin_number = bin(number)
        bin_number = bin_number[2:]
        if is_palindromic(bin_number):
            total += number

print(total)

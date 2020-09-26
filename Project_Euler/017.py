ans = 0
name = ''
dic = {1: 'one',
       2: 'two',
       3: 'three',
       4: 'four',
       5: 'five',
       6: 'six',
       7: 'seven',
       8: 'eight',
       9: 'nine',
       10: 'ten',
       11: 'eleven',
       12: 'twelve',
       13: 'thirteen',
       14: 'fourteen',
       15: 'fifteen',
       16: 'sixteen',
       17: 'seventeen',
       18: 'eighteen',
       19: 'nineteen',
       20: 'twenty',
       30: 'thirty',
       40: 'forty',
       50: 'fifty',
       60: 'sixty',
       70: 'seventy',
       80: 'eighty',
       90: 'ninety',
       0:  ''}


for number in range(1, 1000):
    
    if number > 99:
        name += dic[number // 100] + 'hundred'
    
    if number % 100 > 0:
        if number > 99:
            name += 'and'
        
        if dic.get(number % 100):
            name += dic[number % 100]
        else:
            name += dic[((number % 100) // 10) * 10]
            name += '' + dic[number % 10]
            
    ans += len(name)
    name = ''
    
ans += len('onethousand')


print(ans)

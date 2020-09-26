file = open('import_042.txt')
words = file.read()
words = words.replace('"', '')
words = words.split(',')
file.close()

abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
words_num = []

for word in words:
    summ = 0
    for letter in word:
        summ += abc.index(letter) + 1
    words_num.append(summ)
 
max_words_num = max(words_num)
triangle_number = 0
i = 1
qty = 0

while triangle_number < max_words_num:
    triangle_number = 1 / 2 * i * ( i + 1 )
    qty += words_num.count(triangle_number)
    i += 1

print(qty)

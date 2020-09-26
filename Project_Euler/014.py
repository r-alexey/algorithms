book = {1: 1}

def len_Collatz(number):
    global book
    
    if not book.get(number):    # i.e. we do not know the length of the sequence
        next_number = number
        if next_number % 2 == 0:
            next_number /= 2
        else:
            next_number = next_number * 3 + 1 
        book[number] = len_Collatz(next_number) + 1
        
    return book[number]


longest_sequence = 1
number = 0

for i in range (2, 1000001):
    sequence = len_Collatz(i)
    if sequence > longest_sequence:
        longest_sequence = sequence
        number = i


print(number)

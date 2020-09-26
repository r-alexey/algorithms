x = 1
y = 1

letters = 1
num_of_term = 2

while True:
    
    x, y = y, y + x
    num_of_term += 1
    
    letters = len(str(y))
    
    if letters >= 1000:
        print (num_of_term)
        break

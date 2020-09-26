total = 1
number = 1
side = 1

while True:

    side += 2
    
    for i in ('right', 'down', 'left', 'up'):
        number += side - 1
        total += number
    
    if side == 1001:
        break


print(total)

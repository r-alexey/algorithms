file = open('import_022.txt')
names = file.read()
names = names.replace('"', '')
names = names.split(',')
file.close()
abc = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z', 'A', 'E', 'I', 'O', 'U', 'Y']

names.sort()
abc.sort()
total = 0

for name in names:
    points = 0
    for letter in name:
        points += abc.index(letter) + 1
    points *= names.index(name) +1
    total += points

print(total)

array = [[1]*21]*21

for i in range(1, 21):
    for j in range(1, 21):
        array[i][j] = array[i][j-1] + array[i-1][j]

print (array[20][20])

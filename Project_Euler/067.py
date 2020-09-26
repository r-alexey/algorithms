# ------------- to start, upload data ------------- #

file = open('import_067.txt')
trg = []

for row in file:

    processing_row = row.split(' ')
    result_row = []
    
    for number in processing_row:
        if number[0] == '0':
            result_row.append(int(number[1]))
        else:
            result_row.append(int(number[0:2]))
    
    trg.append(result_row)
    
file.close()


# ------------ now, the main algorithm ------------ #

trg.reverse()
''' 
now, we have such a triangle:
[x x x]
 [x x]
  [x]
and the idea of the algorithm can be represented as follows:
step 1 - select the zero element of the row (i will name it "processing element")
step 2 - find the largest "parent" of processing element
step 3 - add largest "parent" to processing element
step 4 - go to next element of the row
step 4 - after processing the row - go to the next row etc.
'''

for row in range(1, len(trg)):              
    for itm in range( len(trg[row]) ):      # itm - element number
        
        if trg[row-1][itm] > trg[row-1][itm+1]:
            trg[row][itm] += trg[row-1][itm]
        else:
            trg[row][itm] += trg[row-1][itm+1] 
                
print(trg[ len(trg)-1 ])

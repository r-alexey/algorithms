#______________FIRST_WAY______________#
total = 2
old = 1
act = 2

while True:
    old, act = act, old + act
    if act >= 4000000:
        break
    if act % 2 == 0:	
        total += act

print(total)


#_____________SECOND_WAY_____________#
total = 2
old = 1
act = 2

while True:
	old, act = old + act * 2, old * 2 + act * 3
	if act >= 4000000:
		break
	total += act

print(total)

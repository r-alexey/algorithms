#______________FIRST_WAY______________#

List = [i for i in range(2000001)]
List[1] = 0

for Item in List:
	if Item != 0:
	
		for ZeroItem in List[Item * 2 :: Item]:
			List[ZeroItem] = 0

print(sum(List))


#_____________SECOND_WAY_____________#

def search_not_zero(List, Item): 
    try:
        while List[Item] == 0:
            Item += 1
        return Item
    except IndexError:
        return Item

def correcting_list(List, Item):
    for ZeroItem in List[Item * 2 :: Item]:
        List[ZeroItem] = 0
    return List

List = [i for i in range(2000001)]
List[1] = 0
Item = 0

while Item < 2000000:
    Item = search_not_zero(List, Item)
    List = correcting_list(List, Item)
    Item += 1

print (sum(List))

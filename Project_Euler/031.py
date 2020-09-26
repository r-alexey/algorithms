# ---------------------------------------- WAY 1 - LOOPS ---------------------------------------- #

def qty_list(undestr, number):
    return [i for i in range((undestr // number) + 1)]
    
def get_undestr(last_undestr, number, qty):
    return last_undestr - number * qty


ans = 0
undestr200 = 200


for qty200 in qty_list(undestr200, 200):

    undestr100 = get_undestr(undestr200, 200, qty200)
    for qty100 in qty_list(undestr100, 100):
        
        undestr50 = get_undestr(undestr100, 100, qty100)
        for qty50 in qty_list(undestr50, 50):
        
            undestr20 = get_undestr(undestr50, 50, qty50)
            for qty20 in qty_list(undestr20, 20):
            
                undestr10 = get_undestr(undestr20, 20, qty20)
                for qty10 in qty_list(undestr10, 10):
                    
                    undestr5 = get_undestr(undestr10, 10, qty10)
                    for qty5 in qty_list(undestr5, 5):
                        
                        undestr2 = get_undestr(undestr5, 5, qty5)
                        for qty2 in qty_list(undestr2, 2):
                            
                            ans += 1


print(ans)

# ---------------------------------------- WAY 2 - RECURSION ---------------------------------------- #

def qty_list(undestr, number):
    return [i for i in range((undestr // number) + 1)]
    
def get_undestr(last_undestr, number, qty):
    return last_undestr - number * qty

def loop(undestributed, coin_list, index):
    global  ans
    if coin_list[index] == 2:
        ans += len(qty_list(undestributed, coin_list[index]))
    else:
        for qty in qty_list(undestributed, coin_list[index]):
            new_undestributed = get_undestr(undestributed, coin_list[index], qty)
            loop(new_undestributed, coin_list, index + 1)

            
undestributed = 200
coin_list = [200, 100, 50, 20, 10, 5, 2]
index = 0
ans = 0

loop(undestributed, coin_list, index)


print(ans)

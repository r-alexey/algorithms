from itertools import permutations

array = '0123456789'
all_combinations = permutations(array)
all_combinations = list(all_combinations)

ans = ''.join(all_combinations[999999])
print(ans)

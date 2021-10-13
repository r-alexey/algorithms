def return_n_prime_number(n):
   
    prime_number_list = [2]
    prime_number_qty = 1
    current_number = 2
   
    while prime_number_qty < n:
       
        current_number += 1
        is_prime = True
       
        for prime in prime_number_list:
            if current_number % prime == 0:
                is_prime = False
                break
               
        if is_prime:
            prime_number_list.append(current_number)
            prime_number_qty += 1
   
    return current_number

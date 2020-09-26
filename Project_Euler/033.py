total_numerator = 1
total_denominator = 1

for numerator in range(10, 99):
    for denominator in range(numerator + 1, 100):
        
        if (numerator % 10 != 0) and (denominator % 10 != 0):
            
            numerator_str = [i for i in str(numerator)]
            denominator_str = [i for i in str(denominator)]
            total_number = list(set(numerator_str) & set(denominator_str))
            
            if len(total_number) == 1:
                
                numerator_str.remove(total_number[0])
                denominator_str.remove(total_number[0])
                
                quotient_1 = numerator / denominator
                quotient_2 = int(numerator_str[0]) / int(denominator_str[0])
                
                if quotient_1 == quotient_2:
                    total_numerator = total_numerator * numerator
                    total_denominator = total_denominator * denominator


print(total_numerator, '/', total_denominator) # => ans = 100

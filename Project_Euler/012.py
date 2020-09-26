# triangle number generation
def Triangle_number(i):
        t_num = 1 / 2 * i * ( i + 1 )
        return(int(t_num))

		
# take a list of prime factors
def List(t_num):
        factor = 2
        list_ = []
        while True:
                if t_num % factor == 0:
                        list_.append(factor)
                        t_num /= factor
                        factor = 2
                else:
                        factor+=1
                if t_num == 1:
                        list_ = sorted(list_)
                        return list_

						
# quantity of prime factors
def Quantity(list_):
        quantity = []
        elements = set(list_)
        for i in elements:
                quantity.append(list_.count(i))
        return quantity

		
# result
def Result(quantity):
        result = 1
        for i in quantity:
                result *= i + 1
        return result

		
i=1
while True:
        t_num = Triangle_number(i)
        list_ = List(t_num)
        quantity = Quantity(list_)
        result = Result(quantity)
		
        if result < 500:
                i += 1
                continue
        else:
                break
				
            
print(t_num)
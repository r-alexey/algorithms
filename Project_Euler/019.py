years = [i for i in range(1901, 2001)]
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_week = 7
qty = 0

# for the 1900 year
for month in months:
    days = [i for i in range(1, month + 1)]
        
    for day in days:
        if day_of_week == 7:
            day_of_week = 1
        else:
            day_of_week += 1

# for other years
for year in years:
    if year % 4 == 0:
        months [1] = 29
    else: 
        months [1] = 28

    for month in months:
        days = [i for i in range(1, month + 1)]
        
        for day in days:
            if day_of_week == 7:
                day_of_week = 1
            else:
                day_of_week += 1
            
            if day_of_week == 7 and day == 1:
                qty += 1


print (qty)

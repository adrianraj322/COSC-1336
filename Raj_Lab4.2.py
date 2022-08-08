#Adrian Raj, Status-Complete
#Create a table where you can see the ocean's level rise by 1.8 millimeters per year for 25 years.

#Enter the default amounts.

year = 25

total_millimeters = 0.0

rise_per_year = 1.8

#Enter the table

print('Year\t\tRise (in millimeters)')
print('---------------------------------------------')

for year in range(1, 26, 1):
    total_millimeters = year * rise_per_year
    year -= 1
    print((year + 1), '\t\t', format(total_millimeters, ',.2f'))
    

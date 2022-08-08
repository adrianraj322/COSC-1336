#Adrian Raj, Status-Complete
#Determine what how many packages you want, the total discount amount, the total amount of the package with the discount, and the final amount.

package_price = 149
quantity = float(input('Enter the amount of packages you want: '))

if quantity < 0:

    print('Error!')

else:

    discount_rate = 0

if quantity < 10:

    discount_rate = 0

elif quantity >= 10 and quantity <= 49:

    discount_rate = 0.1

elif quantity >= 50 and quantity <= 99:

    discount_rate = 0.2

elif quantity >= 100 and quantity <= 149:

    discount_rate = 0.3

elif quantity >= 150:

    discount_rate = 0.4

package_total = package_price * quantity
discount_total = package_total * discount_rate
final_total = package_total - discount_total

print('Your total amount is $ ' + format(package_total, ',.2f'))
print('Your discount rate is ' + format(discount_rate, ',.2f'))
print('Your total discount is $' + format(discount_total, ',.2f'))
print('Your final total is $' + format(final_total, ',.2f'))



#Adrian Raj, Status-Complete
#Create a loop where you enter a monthly budget and how much you spent that month.

#Enter the default amounts.
expense = 0.0
budget = 0.0
difference = 0.0
total_expense = 0.0
yes = 'y'
repeat = 'r'

while repeat == 'r':
    
    #Enter your budget and your expenses.
    budget = float(input('What is your budget for the month? $'))

    while yes == 'y':
        expense = float(input('Monthly expense amount? $'))
        total_expense = total_expense + expense
        yes = input('Do you have any other expenses? (Enter y for yes.)')

    #Enter the calculations for your amounts.
    if total_expense < budget:
        difference = budget - total_expense
        print('Your difference is $', format(difference, ',.2f') , 'under budget.')

    elif total_expense > budget:
        difference = total_expense - budget
        print('Your difference is $', format(difference, ',.2f') , 'over budget.')
    
    else:
        print('You are right on budget.')

    #Enter the repeat function.
    repeat = input('Do you want to enter another budget and expense/s?' \
                   '(Enter r for repeat): ')

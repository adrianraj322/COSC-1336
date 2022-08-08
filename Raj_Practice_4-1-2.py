#Prepare the variable 'repeat' for the loop.
repeat = 'r'
while repeat == 'r':

    #Enter two numbers of your choice.
    num_1 = float(input('Enter your first number: '))
    num_2 = float(input('Enter your second number: '))

    #Calculate the sum of the two numbers.
    num_sum = num_1 + num_2

    #Display the sum.
    print('The sum is ', \
          format(num_sum, ',.2f'))

    #Repeat the process if you want to.
    repeat = input('Do you want to get another sum?' \
                    ' (Enter r for repeat): ')

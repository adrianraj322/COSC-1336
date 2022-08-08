#Prepare the variable 'repeat' for the loop.
repeat = 'r'
while repeat == 'r':

    #Input a number between 1-7.
    number = int(input('Enter a number between 1-7: '))

    #Make if-elif-if statements to identify the numbers with days.
    if number == 1:

        print('Monday')

    elif number == 2:
        
         print('Tuesday')
         
    elif number == 3:
    
         print('Wednesday')
 
    elif number == 4:
    
         print('Thursday')
 
    elif number == 5:
    
         print('Friday')
 
    elif number == 6:
    
         print('Saturday')
 
    elif number == 7:
    
         print('Sunday')
 
    elif number < 1 or number > 7:
    
         print('Error!')

#Repeat the process if necessary using the variable 'r'
    repeat = input('Do you want to type in another number?' \
                    ' (Enter r for repeat): ') 

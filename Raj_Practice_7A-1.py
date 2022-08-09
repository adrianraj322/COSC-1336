#################################################################################
#                                                                               #
#   Adrian Raj, Status-Complete                                                 #
#                                                                               #
#   Create a couple of loops that print out seven random numbers in one column. #
#                                                                               # 
#################################################################################

#Import the random module.
import random

#Create brackets to contain the numbers.
lottery_numbers = []

#Create random numbers from 0 to 9 in seven row.
for row in range(7):
    
    lottery_numbers.append(random.randint(0, 9))

    #Create one column for the numbers to be in.
    for col in range(1):
        
        print(lottery_numbers[row], end = '')



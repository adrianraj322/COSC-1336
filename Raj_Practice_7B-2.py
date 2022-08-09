#########################################################################
#                                                                       #
#   Adrian Raj, Status-Complete                                         #
#                                                                       #
#   Create a function that inputs 12 random numbers into a 2-D list     #
#                                                                       # 
#########################################################################

#Import the random module
import random

#Enter the default amount of rows and columns
row = 3
col = 4

#Create a main function that engulfs the entire program
def main():

    total = 0

    #Create the base of the 2-D list
    values = [[0, 0, 0, 0],

        [0, 0, 0, 0],

        [0, 0, 0, 0]]


    #Enter random numbers for the rows and columns
    for r in range(row):

        for c in range(col):

            values[r][c] = int(input('Enter a random number: '))


    print()
    print(values)

    #Add the total amount of random numbers
    for r in range(row):

        for c in range(col):

            total += values[r][c]

    print()
    print('The total amount of all random numbers is', total)

#End the program with main()
main()

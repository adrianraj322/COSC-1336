##############################################################################################################################
#                                                                                                                            #
#   Adrian Raj, Status-Complete                                                                                              #
#                                                                                                                            #
#   Create a couple of functions that print out a list, the constant number, and the values greater than the constant number #
#                                                                                                                            # 
##############################################################################################################################

#Create a main function for the entire program
def main():

    #Initialize list1 and list2
    list1 = []
    list2 = list1

    #Ask user for number of items in list1
    items_in_list = int(input('How many numbers do you want? '))

    #Ask user for items in rows
    for row in range(1, items_in_list + 1):
        integer = int(input('Enter a number: '))
        list1.append(integer)

    #Print list1 in a column
    for col in range(1):
        print(list1, sep = ',')

    #Give n an integer value
    n = int(input('Enter a constant number: '))

    #Call the display_larger function
    display_larger(list1, list2, n)

#Create a sub-function to take values greater than n as list2
def display_larger(list1, list2, n):

    #Create a for-loop to remove items less than n
    for item in list(list2):
        if item < n:
            list2.remove(item)

    #Enter ending statements
    print()
    print('The list is', list1)
    print('The constant number is', int(n))
    print('The list of numbers greater than n is', list2)
    
#End the program off with main()
main()

    

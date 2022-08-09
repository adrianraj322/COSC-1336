#################################################################################################
#                                                                                               #
#   Adrian Raj, Status-Complete                                                                 #
#                                                                                               #
#   Create a main function that creates two lists and outputs the results from the sub-function #
#                                                                                               # 
#################################################################################################

#Create a main function that engulfs the entire program
def main():

    #Create two lists with 5 integers in them
    list1 = [4, 9, 29, 41, 3]
    list2 = [12, 68, 39, 1, 19]
    list3 = list1[:] + list2[:]

    #Print out the two lists combined, their minimum value, and their maximum value
    print('The two lists combined is', list3)
    print('The total value of the two lists is', total_list(list3))
    print('The minimum of the two lists is', min(list3))
    print('The maximum of the two lists is', max(list3))

#Create a sub-function to find the total value of the two lists
def total_list(list3):
    total = sum(list3)
    return total

#End the program with main()
main()

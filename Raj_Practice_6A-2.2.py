################################################################
#                                                              #
#   Adrian Raj, Status-Complete                                #
#                                                              #
#   Create a main funcion that displays your amount of numbers #
#                                                              # 
################################################################

#Create a main function that engulfs the entire program
def main():

    #Connect the .txt file to the program
    number_list_file = open('number_list.txt', 'r')

    #Create a for-loop that displays all the numbers on the .txt file
    for line in number_list_file:
        number = float(line)
        print(format(number, ',.2f'))

    #Turn off the connection between the .txt file and the program
    number_list_file.close()

#Finish the program off with main()
main()


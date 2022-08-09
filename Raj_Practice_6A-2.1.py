#################################################################
#                                                               #
#   Adrian Raj, Status-Complete                                 #
#                                                               #
#   Create a main funcion that inputs how many numbers you want #
#                                                               # 
#################################################################

#Create a main function that engulfs the entire program
def main():

    #Create an intro statement telling the user how many numbers you want to input
    intro_statement = int(input('How many numbers do you want? '))

    #Connect the .txt file and the program
    number_list_file = open('number_list.txt', 'w')

    #Create a for-loop to input the numbers you want starting from 1.
    for count in range(1, intro_statement + 1):
        count = str(count)
        number_list_file.write(str(count) + '\n')

    #Turn off the connection between the .txt file and the program
    number_list_file.close()

    print('Numbers have been written to number_list.txt.')

#Finish the program off with main()
main()

#########################################################################################################
#                                                                                                       #
#   Adrian Raj, Status-Complete                                                                         #
#                                                                                                       #
#   Create a main funcion that asks for your age, name, and friend's name, and writes it on a .txt file #
#                                                                                                       # 
#########################################################################################################

#Create a main function that engulfs the entire program
def main():

    #Create an intro statement to ask for how many sets you want
    intro_statement = int(input('How many sets of inputs do you want? '))

    #Connect the .txt file to the program
    my_name_file = open('my_name.txt', 'w')

    #Create a for-loop for every set of inputs
    for count in range(1, intro_statement + 1):
        print('Enter data for statements')
        my_name = input('Enter your name: ')
        my_age = input('Enter your age: ')
        friends_name = input("Enter your friend's name: ")

        #Add a newline character for the variables
        my_name_file.write(my_name + '\n')
        my_name_file.write(my_age + '\n')
        my_name_file.write(friends_name + '\n')

    #Turn off the connection between the .txt file and the program
    my_name_file.close()

    print('Statements have been written to my_name.txt.')

#Finish the program off with main()
main()

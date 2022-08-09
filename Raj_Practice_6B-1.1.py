######################################################################
#                                                                    #
#   Adrian Raj, Status-Complete                                      #
#                                                                    #
#   Create a main funcion that displays the student's name and score #
#                                                                    # 
######################################################################

#Create a main function that engulfs the entire program.
def main():

    #Create an intro statement for the program.
    intro_statement = int(input('How many scores do you want to create? '))

    #Connect the program and the .txt file.
    students_file = open('students.txt', 'w')

    #Create a loop to input the name and score based on how many you want.
    for count in range(1, intro_statement + 1):
        print('Enter data for student')
        name = input('Name: ')
        score = input('Score: ')

        #Take out the newline characters on the name and score lines.
        students_file.write(name + '\n')
        students_file.write(score + '\n')

    #Turn off the connection between the program and .txt file.
    students_file.close()
    
    print('Student records written to students.txt.')

#End the program of with main().
main()

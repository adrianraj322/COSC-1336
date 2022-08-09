######################################################################
#                                                                    #
#   Adrian Raj, Status-Complete                                      #
#                                                                    #
#   Create a main funcion that displays the names and scores in IDLE #
#                                                                    # 
######################################################################

#Create a main function that engulfs the entire program.
def main():

    #Connect the .txt file and the program.
    students_file = open('students.txt', 'r')

    #Create the name line to be displayed in the program.
    name = students_file.readline()

    #Create a while loop programmed to create the score line after the name line has been displayed.
    while name != '':

        #Create the store line.
        score = students_file.readline()

        #Take out the newline characters.
        name = name.rstrip('\n')
        score = score.rstrip('\n')
        
        print('Name:', name)
        print('Score:', score)

        #Repeat the name line process after the first score line has been displayed.
        name = students_file.readline()

    #Turn off the connection between the .txt file and the program.
    students_file.close()

#Finish the program off with main().
main()

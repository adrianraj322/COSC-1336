#######################################################################################################################
#                                                                                                                     #
#   Adrian Raj, Status-Complete                                                                                       #
#                                                                                                                     #
#   Create a function with three dictionaries of classes, their rooms, instructors, and times and display the results #
#                                                                                                                     # 
#######################################################################################################################

#Create a main function
def main():

    #Initialize repeat
    repeat = 'r'
    while repeat == 'r':

        #Initialize course_number
        course_number = input('Enter a course number or press enter to stop: ')

        #Label the dictionaries with data
        room = {'CS101': '3004', 'CS102': '4501', 'CS103': '6755',
                'NT110': '1244', 'CM241': '1411'}

        instructor = {'CS101': 'Haynes', 'CS102': 'Alvarado', 'CS103': 'Rich',
                      'NT110': 'Burke', 'CM241': 'Lee'}

        time = {'CS101': '8:00 am', 'CS102': '9:00 am', 'CS103': '10:00 am',
                'NT110': '11:00 am', 'CM241': '1:00 pm'}

        #Create an if statement that corresponds the course number to its information
        if course_number in room:

            print()
            print('The details for course', course_number, 'are: ')
            print('Room:', room[course_number])
            print('Instructor:', instructor[course_number])
            print('Time:', time[course_number])
            print()
            repeat = input('Do you want to enter another course number? (Enter r for repeat): ')

        #Create an else statement if there is no class number in the dictionary
        else:

            print('That class does not exist.')

#Finish the program off with main()
main()

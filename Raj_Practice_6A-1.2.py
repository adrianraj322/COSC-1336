#################################################################################
#                                                                               #
#   Adrian Raj, Status-Complete                                                 #
#                                                                               #
#   Create a main function where you can display the text from the .txt file                                                       #
#                                                                               # 
#################################################################################

#Create a main function that engulfs the entire program
def main():

    #Connect the .txt file and the program
    infile = open('my_name.txt', 'r')

    #Set the statements for display in the program
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    #Strip the newline characters 
    line1 = line1.rstrip('\n')
    line2 = line2.rstrip('\n')
    line3 = line3.rstrip('\n')

    #Turn off the connection between the .txt file and the program
    infile.close()

    #Print out the statements
    print(line1)
    print(line3)
    print('My age is:', line2)
    print('My age divided by 2 is:', int(line2) // 2)

#Finish the program off with main()
main()
                

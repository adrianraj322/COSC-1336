############################################################################################
#                                                                                          #
#   Adrian Raj, Status-Complete                                                            #
#                                                                                          #
#   #Create a function where you can calculate the sum and the average of numbers 1 to 100 #
#                                                                                          # 
############################################################################################


#Create a main function that engulfs the entire program.
def main():

    #Enter the try function to make the except functions work.
    try:
        
        #Enter the default total.
        total = 0.0

        #Connect the .txt file and the program.
        number_list_file = open('number_list.txt', 'r')

        #Create a for-loop that calculates the sum and the average.
        for line in number_list_file:
            num_sum = float(line)
            total += num_sum
            average = total / float(line)

        #Turn off the connection between the .txt file and the program.
        number_list_file.close()

        #Print out the sum and average to the hundreths place.
        print('The sum is', format(total, ',.2f'))
        print('The average is', format(average, ',.2f'))

    #Enter the except functions where if an error occurs, the following statements will be displayed.
    except IOError:
        print('A reading error occured.')

    except ValueError:
        print('A non-numeric data error occured.')

    except:
        print('An error occured.')
        
#Finish the program off with main().
main()
    

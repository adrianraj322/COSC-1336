#Adrian Raj, Status-Complete
#Create a function that takes the random numbers from the .txt file and adds them all up

#Create a main function that engulfs the entire program
def main():

    #Enter a try function to make the except functions work
    try:

        #Enter the default total
        total = 0.0

        #Connect the program to the .txt file
        random_numbers_file = open('random_numbers.txt', 'r')

        #Create a for-loop that adds the numbers up and changes the total to the sum
        for line in random_numbers_file:
            num_sum = float(line)
            total += num_sum

        #Turn off the connection between the program and the .txt file
        random_numbers_file.close()

        #Print the final total to the hundreths place
        print('The sum is', format(total, ',.2f'))

    #Enter the except functions
    except IOError:
        print('A reading error occured.')

    except ValueError:
        print('A non-numeric data error occured.')

    except:
        print('An error occured.')

#Finish the program off with main()
main()

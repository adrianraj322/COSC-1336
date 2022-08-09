#Adrian Raj, Status-Complete
#Create a function that makes you input random numbers and exports them to the .txt file

#Import the random module to connect the program to random numbers
import random

#Create a main function that engulfs the entire program
def main():

    #Enter a try function to make the except functions work
    try:

        #Connect the program to the .txt file
        random_numbers_file = open('random_numbers.txt', 'w')

        #Enter an intro statement to ask you how many random numbers you want to put in 
        intro_statement = int(input('How many numbers do you want to create? '))
            
        #Create a for-loop based on your amount of random numbers
        for number in range(1, intro_statement + 1):
            number = random.randint(1, 500)

            random_numbers_file.write(str(number) + '\n')

        #Turn off the connection between the .txt file and the program
        random_numbers_file.close()

        #Print the outro to confirm that your numbers have been exported to the .txt file
        print('Random numbers written to random_numbers.txt.')

    #Enter your except functions
    except IOError:
        print('A reading error occured.')

    except ValueError:
        print('A non-numeric data error occured.')

    except:
        print('An error occured.')

#Finish the program off with main()
main()

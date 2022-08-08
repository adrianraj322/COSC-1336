#Adrian Raj, Status-Complete
#Create a program of two functions which converts kilometers to miles.

#Label the magic number variable with its value.
magic_number = 0.6214

#Create a main function that engulfs the entire program.
def main():
    intro()
    kilometers_needed = int(input('Enter the number of kilometers: '))
    kilometers_to_miles(kilometers_needed)
    

#Create an intro statement to the program.
def intro():
    print('This program converts kilometers to miles.')
    print('The formula is miles = 0.6214 * kilometers.')
    print()

#Create a conversion equation to convert kilometers to miles.
def kilometers_to_miles(kilometers):
    miles = kilometers * magic_number
    print('That converts to', format(miles, ',.2f'), 'miles.')

main()

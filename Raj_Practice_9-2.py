###############################################################################################################################
#                                                                                                                             #
#   Adrian Raj, Status-Complete                                                                                               #
#                                                                                                                             #
#   Create a dictionary where you can create dishes, send it to a .txt file, and import it from there using the pickle module #
#                                                                                                                             # 
###############################################################################################################################

import pickle

#Initialize choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
SAVE = 5
DISPLAY = 6
QUIT = 7

#Create a main function for the menu
def main():
    
    #Create an empty dictionary.
    dishes = {}

    #Initialize a variable for the user's choice
    choice = 0

    #Create a while loop for the choices
    while choice != QUIT:
        
        #Get the user's menu choice
        choice = get_menu_choice()

        if choice == LOOK_UP:
            
            look_up(dishes)
            
        elif choice == ADD:
            
            add(dishes)
            
        elif choice == CHANGE:
            
            change(dishes)
            
        elif choice == DELETE:
            
            delete(dishes)

        elif choice == SAVE:

            save(dishes)

        elif choice == DISPLAY:

            display(dishes)

#Create a function for the displayed options
def get_menu_choice():
    print()
    print('Friends and Their Birthdays')
    print('---------------------------')
    print('1. Look up a price')
    print('2. Add a new price')
    print('3. Change a price')
    print('4. Delete a price')
    print('5. Save the price')
    print('6. Display the price')
    print('7. Quit the program')
    print()

    #Get the user's choice
    choice = int(input('Enter your choice: '))

    #Validate the choice
    while choice < LOOK_UP or choice > QUIT:
        
        choice = int(input('Enter a valid choice: '))

    #Return the user's choice to the other functions
    return choice

#Create a function to look up a dish and its price
def look_up(dishes):

    #Input the name of the dish
    name = input('Enter a name: ')

    #Look it up in the dictionary
    print(dishes.get(name, 'Not found.'))

#Create a function to add a dish and its price
def add(dishes):

    #Initialize the dish's name and price
    name = input('Enter a name: ')
    price = input('Enter a price: ')

    #If the name does not exist, add it.
    if name not in dishes:
        
        dishes[name] = price
        
    else:
        
        print('That entry already exists.')

#Create a function to change a dish and its price
def change(dishes):

    #Initialize the dish's name
    name = input('Enter a name: ')

    if name in dishes:

        #Create a new price 
        price = input('Enter the new price: ')

        #Update the entry
        dishes[name] = price
        
    else:
        
        print('That entry does not exist')

#Create a function that deletes a dish and its price
def delete(dishes):

    #Initialize the name
    name = input('Enter a name: ')

    #If the name is found, delete the entry.
    if name in dishes:
        
        del dishes[name]
        
    else:
        
        print('That entry does not exist.')

#Create a function that accepts data and will be stored in a file
def save(dishes):

    #Initialize the repeat variable for more data
    repeat = 'r'

    #Open dishes.txt to export data
    dishes_output_file = open('dishes.txt', 'wb')
    
    while repeat.lower() == 'r':

        save_data(dishes_output_file)

        repeat = input('Enter more data? (Enter r for repeat): ')

    dishes_output_file.close()

#Create a function that asks for the name and price in a specific format
def save_data(dishes_output_file):

    dishes = {}

    dishes['name'] = input('Enter a name: ')
    dishes['price'] = input('Enter a price: ')

    #Export the dishes to dishes.txt
    pickle.dump(dishes, dishes_output_file)

#Create a function that displays your dishes in the program
def display(dishes):

    end_of_file = False

    #Connect the .txt file and the program
    dishes_input_file = open('dishes.txt', 'rb')

    while not end_of_file:
        
        try:

            #Import the data from the .txt file
            dishes = pickle.load(dishes_input_file)

            display_data(dishes)

        except EOFError:

            end_of_file = True

    dishes_input_file.close()

#Create a function that labels the name and price in a specific format
def display_data(dishes):

    print('Name: ', dishes['name'])
    print()
    print('Price: ', dishes['price'])

#End the program off with main()
main()

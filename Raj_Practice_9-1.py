######################################################################################################################
#                                                                                                                    #
#   Adrian Raj, Status-Complete                                                                                      #
#                                                                                                                    #
#   Create a dictionary where you can create dishes and their prices and can add, look up, change, or delete options #
#                                                                                                                    # 
######################################################################################################################

#Initialize choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

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

#Create a function for the displayed options
def get_menu_choice():
    print()
    print('Friends and Their Birthdays')
    print('---------------------------')
    print('1. Look up a price')
    print('2. Add a new price')
    print('3. Change a price')
    print('4. Delete a price')
    print('5. Quit the price')
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

#End the program off with main()
main()

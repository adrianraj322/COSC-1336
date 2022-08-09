##################################################################################################################
#                                                                                                                #
#   Adrian Raj, Status-Complete                                                                                  #
#                                                                                                                #
#   Create a function that imports pet.py into a function where the age, animal type, and name will be displayed #
#                                                                                                                # 
##################################################################################################################

#Import pet.py
import pet

#Create a main function
def main():

    #Initialize name, animal_type, and age
    name = input("Enter the animal's name: ")
    animal_type = input("Enter the animal's type: ")
    age = input("Enter the animal's age: ")

    #Create an object of Class Pet
    pets = pet.Pet(name, animal_type, age)

    #Enter final statements
    print('Here is the data you entered:')
    print()
    print(pets)

#Finish program off with main()
main()

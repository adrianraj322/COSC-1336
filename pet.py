#####################################################################
#                                                                   #
#   Adrian Raj, Status-Complete                                     #
#                                                                   #
#   Create a class that defines a pet's name, animal type, and age  #
#                                                                   # 
#####################################################################

#Create Class Pet
class Pet:

    #Initialize name, animal_type, and age
    def __init__(self, name, animal_type, age):

        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    #Set the variables for inputting
    def set_name(self, name):
        
        self.__name = name

    def set_animal_type(self, animal_type):
        
        self.__animal_type = animal_type

    def set_age(self, age):
        
        self.__age = age

    #Return the variables' inputs
    def get_name(self):
        
        return self.__name

    def get_animal_type(self):
        
        return self.__animal_type

    def get_age(self):
        
        return self.__age

    def __str__(self):

        return "Name: " + self.__name + \
               "\nAnimal Type: " + self.__animal_type + \
               "\nAge: " + self.__age

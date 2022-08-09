################################################################################################################                                                                                                              #
#
#   Adrian Raj, Status-Complete                                                                                #
#                                                                                                              #
#   Create a function that counts the amount of lowercase, uppercase, number, and space characters in a string #
#                                                                                                              # 
################################################################################################################

#Create a main function
def main():

    #Initialize total_lowercase, total_uppercase, total_digits, total_spaces
    total_lowercase = 0
    total_uppercase = 0
    total_digits = 0
    total_spaces = 0

    #Input the user's string
    string = input('Enter your string: ')

    #Create a for-loop to count the characters
    for letter in string:

        if letter.islower():

            total_lowercase += 1

        elif letter.isupper():

            total_uppercase += 1

        elif letter == ' ':

            total_spaces += 1

        elif letter.isdigit():

            total_digits += 1
    

    #Enter ending statements
    print()
    print('The total amount of lowercase letters is', total_lowercase)
    print('The total amount of uppercase letters is', total_uppercase)
    print('The total amount of digits is', total_digits)
    print('The total amount of spaces is', total_spaces)

#Finish off with main()
main()

#########################################################################################
#                                                                                       #
#   Adrian Raj, Status-Complete                                                         #
#                                                                                       #
#   Create a function that turns lowercase and uppercase characters into their opposite #
#                                                                                       # 
#########################################################################################

#Create main function
def main():

    #Input the user's sentence
    original_sentence = input('Enter a sentence: ')

    #Make the new sentence blank
    new_sentence = ''

    #Create a for-loop to input the user's sentence into the new sentence
    for x in original_sentence:

        #Flip the lowercase and uppercase characters
        if(x.isupper()):

            new_sentence += x.lower()

        else:

            new_sentence += x.upper()

    #Enter ending statements
    print()
    print('The original sentence is', original_sentence)
    print('The new sentence is', new_sentence)

#Finish program off with main()
main()

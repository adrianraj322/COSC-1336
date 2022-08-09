###############################################################################################################
#                                                                                                             #
#   Adrian Raj, Status-Complete                                                                               #
#                                                                                                             #
#   Create a function where the user inputs a full name and counts how many a, e, and s characters there are  #
#                                                                                                             # 
###############################################################################################################

#Create a main function
def main():

  #Initialize total_a, total_e, and total_s
  total_a = 0
  total_e = 0
  total_s = 0

  #Ask user for inputs for first_name, middle_name, and last_name
  first_name = input('Enter your first name: ')
  middle_name = input('Enter your middle name: ')
  last_name = input('Enter your last name: ')

  #Combine inputs to create full_name
  full_name = first_name + ' ' + middle_name + ' ' + last_name
  print('Your name is: ', full_name)

  #Create for-loop to count characters in full_name
  for letter in full_name:

      if letter == 'A' or letter == 'a':

          total_a += 1

      if letter == 'E' or letter == 'e':

          total_e += 1

      if letter == 'S' or letter == 's':

          total_s += 1

  #Enter ending statements
  print('The letter a is in the name', total_a, 'times.')
  print('The letter e is in the name', total_e, 'times.')
  print('The letter s is in the name', total_s, 'times.')

#Finish the program off with main()
main()

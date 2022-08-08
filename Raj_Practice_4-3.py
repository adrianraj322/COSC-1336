# Ask the user for a positive integer no greater than 15.
number = int(input('How many rows would you like? (between 1 and 15):'))

while number < 1 or number > 15:

    print('Error!')

    number = int(input('How many rows would you like? (between 1 and 15): '))

#Ask the user for a character.
character = str(input('What character should I use for the drawing? '))

#Displaying the pattern

print('')

for row in range (number):

	for col in range (number):

		print(character, end = '')

	print()

print('')

#Adrian Raj, Status-Complete
#Create a main function that can generate random integers and import another Python file.

#Import random numbers and import from square.py.
import random
from square import square_area, square_perimeter

#Create the main function with random integers from 1 to 100.
def main():
    square_side = random.randint(1, 100)
    print('The side of the square is', square_side)
    print("The square's area is", square_area(square_side))
    print("The square's perimeter is", square_perimeter(square_side))

#End the program with main().
main()

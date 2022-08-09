#Adrian Raj, Status-Complete
#Create two functions that gives you a random radius and the area of the circle by using a return function.

#Import random to activate the random numbers module.
import random

#Create a main function to print out the radius and area.
def main():
    radius = random.uniform(1, 100)
    print('The radius is', format(radius, ',.2f'))
    print('The area is', format(area(radius), ',.2f'))

#Create another function to calculate the area of a circle based on the radius.
def area(radius):
    return 3.14 * radius ** 2

#Finish the program off by entering main().
main()

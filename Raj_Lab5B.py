#################################################################################
#                                                                               #
#   Adrian Raj, Status-Complete                                                 #
#                                                                               #
#   Create the main function which imports distance.py and print out the table  #
#                                                                               # 
#################################################################################


#Import the falling_distance function from distance.py
from distance import falling_distance

#Create the main function
def main():
    
    print('Time\tFalling Distance')
    print('----------------------------------------')

    #Enter the default amounts
    gravitational_constant = 9.8

    time = 0

    meters_per_second = time ** 2

    #Input the falling_distance function in the main function
    falling_distance(gravitational_constant, time)

    #Create a for-loop from 1-10 that inputs the number of seconds and the falling distance
    for time in range(1, 11):

        print(time, '\t', format(falling_distance(gravitational_constant, time), '.2f'))

#End the program with main()
main()

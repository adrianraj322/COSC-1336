###################################################################################################################
#                                                                                                                 #
#   Adrian Raj, Status-Complete                                                                                   #
#                                                                                                                 #
#   Create a function that gives the data for three employees by their name, ID number, department and job title  #
#                                                                                                                 # 
###################################################################################################################

#Import employee.py
import employee

#Create a main function
def main():

    #Give the variables a set of inputs
    employee_number = input('Enter the employee #: ')
    name = input("Enter the employee's name: ")
    id_number = input("Enter the employee's ID number: ")
    department = input("Enter the employee's department: ")
    job_title = input("Enter the employee's job title: ")

    print()
    print()

    employee_number2 = input('Enter the employee #: ')
    name2 = input("Enter the employee's name: ")
    id_number2 = input("Enter the employee's ID number: ")
    department2 = input("Enter the employee's department: ")
    job_title2 = input("Enter the employee's job title: ")

    print()
    print()

    employee_number3 = input('Enter the employee #: ')
    name3 = input("Enter the employee's name: ")
    id_number3 = input("Enter the employee's ID number: ")
    department3 = input("Enter the employee's department: ")
    job_title3 = input("Enter the employee's job title: ")

    #Put the variables from the class Employee to another variables
    employee1 = employee.Employee(employee_number, name, id_number, department, job_title)
    employee2 = employee.Employee(employee_number2, name2, id_number2, department2, job_title2)
    employee3 = employee.Employee(employee_number3, name3, id_number3, department3, job_title3)

    #Print out the variables
    print('Here is the data you entered:')
    print()
    print(employee1)
    print()
    print(employee2)
    print()
    print(employee3)

#Finish off the program with main()
main()

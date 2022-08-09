###########################################################################################
#                                                                                         #
#   Adrian Raj, Status-Complete                                                           #
#                                                                                         #
#   Create a class that defines an employee's name, id number, department, and job title  #
#                                                                                         # 
###########################################################################################

#Create Class Employee
class Employee:

    #Initialize name, id_number, department, and job_title
    def __init__(self, employee_number, name, id_number, department, job_title):

        self.__employee_number = employee_number

        self.__name = name
        
        self.__id_number = id_number
        
        self.__department = department
        
        self.__job_title = job_title

    #Set the variables for inputting
    def set_employee_number(self, employee_number):

        self.__employee_number = employee_number
    
    def set_name(self, name):

        self.__name = name

    def set_id_number(self, id_number):

        self.__id_number = id_number

    def set_department(self, department):

        self.__department = department

    def set_job_title(self, job_title):

        self.__job_title = job_title

    #Return the variable's inputs
    def get_employee_number(self):
        
        return self.__employee_number
    
    def get_name(self):

        return self.__name
    
    def get_id_number(self):

        return self.__id_number

    def get_department(self):

        return self.__department

    def get_job_title(self):

        return self.__job_title

    #Define objects as strings
    def __str__(self):

        return "Employee: " + self.__employee_number + \
               "\nName: " + self.__name + \
               "\nID Number: " + self.__id_number + \
               "\nDepartment: " + self.__department + \
               "\nJob Title: " + self.__job_title

        return "Employee: " + self.__employee_number2 + \
               "\nName: " + self.__name2 + \
               "\nID Number: " + self.__id_number2 + \
               "\nDepartment: " + self.__department2 + \
               "\nJob Title: " + self.__job_title2

        return "Employee: " + self.__employee_number3 + \
               "\nName: " + self.__name3 + \
               "\nID Number: " + self.__id_number3 + \
               "\nDepartment: " + self.__department3 + \
               "\nJob Title: " + self.__job_title3
               

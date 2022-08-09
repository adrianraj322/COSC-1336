###########################################################################################################
#                                                                                                         #
#   Adrian Raj, Status-Complete                                                                           #
#                                                                                                         #
#   Create a function that inputs a date in the form mm/dd/yyyy and prints out in the form of mm dd, yyyy #
#                                                                                                         # 
###########################################################################################################

#Create a main function
def main():

    #Initalize my_date
    my_date = input('Enter a date(mm/dd/yyyy): ')
    date_slash = my_date.split('/')

    #Initialize month, day, and year
    month = int(date_slash[0])
    day = int(date_slash[1])
    year = int(date_slash[2])

    #Create if-elif statements that represent numbers 1-12 to their corresponding months
    if month == 1:
    
        month = 'January'
    
    elif month == 2:
        
        month = 'February'
    
    elif month == 3:
    
        month = 'March'
    
    elif month == 4:
    
        month = 'April'
    
    elif month == 5:
        
        month = 'May'
    
    elif month == 6:
    
        month = 'June'
    
    elif month == 7:
    
        month = 'July'
    
    elif month == 8:
    
        month = 'August'
    
    elif month == 9:
    
        month = 'September'
    
    elif month == 2:
    
        month = 'October'
    
    elif month == 2:
    
        month = 'November'
    
    elif month == 12:
    
        month = 'December'

    #Initialize date2
    date2 = month + ' ' + str(day) + ', ' + str(year) 

    print(date2)

#Finish the program off with main()
main()

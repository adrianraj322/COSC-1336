#Adrian Raj, Status-Complete
#Enter a month, day, and year and find out if the date is magic or not.
month = int(input('Enter a month in nuumeric form: '))
day = int(input('Enter a day in numeric form: '))
year = int(input('Enter a two-digit year: '))
magic = day * month

if magic == year:

    print('The date is magic!')

else:

    print('The date is not magic!')

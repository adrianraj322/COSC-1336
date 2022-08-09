#Adrian Raj, Status-Complete
#Create two functions that give you the amount of stars based on your critics' ratings.

#Create a main function that engulfs the entire program.
def main():
 
#Create a for-loop to ask how many rating you want and to enter your rating/s.
 
  num = int(input('How many ratings: '))
 
  num_sum = 0
 
  x = 1
 
  while x <= num:
 
    rating = float(input('Enter your rating: '))
 
    num_sum += rating
 
    x = x + 1
 
    rating_average = num_sum / num
 
    determine_stars(rating_average)
  
#Create a function that determines the amount of stars you deserve.
def determine_stars(rating_average):
 
  if rating_average < 0 or rating_average > 10:
 
    print('Error')
 
  elif rating_average < 5.0 and rating_average >= 0:
 
    print('No stars')
 
  elif rating_average >= 5 and rating_average < 6:
 
    print('*')
 
  elif rating_average >= 6 and rating_average < 7:
 
    print('**')
 
  elif rating_average >= 7 and rating_average < 8:
 
    print('***')
 
  elif rating_average >= 8 and rating_average < 9:
 
    print('****')
 
  elif rating_average >= 9 and rating_average <= 10:
 
    print('*****')
  
#Finish the program off by entering main().
main()

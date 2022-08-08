#Input your low and high numbers.
low_num = int(input('Enter a low Number: '))
high_num = int(input('Enter a high number: '))

#Find the range of your two numbers and multiply each number by 10.
for num in range(low_num, high_num):

    final_num = num * 10

    print(num, '\t', final_num)




#Make a second loop finding the total of the range of your two numbers.
total = 0

for count in range(low_num, high_num):

    total = total + count

print('The total is: ', total)

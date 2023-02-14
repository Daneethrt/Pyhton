num = int(input('How many numbers: '))
total_sum = 0
for n in range(num):
    numbers = float(input('Enter number : '))
    total_sum += numbers
avg = total_sum/num
print('Average is',avg)
if (avg>80):
    print('Grade A')
elif (avg>60):
    print('Grade B')
    
elif (avg>40):
    print('Grade c')
else:
    print('Grade F')

    



age = int(input('Enter your age in years: '))
max_heart_rate = 206.9 - (0.67*age) #ref: Med Sci Sports Exercise
target = 0.64 * max_heart_rate
print('Your target fat-burning heart rate is', target)

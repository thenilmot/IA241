'''
lab 5. If Statement in Python
'''

#3.1
alien_color = 'green'
if alien_color =='green':
    print('player earned 5 points')
    
#3.2
alien_color2 = 'red'
if alien_color2 == 'green':
    print('player earned 5 points')
else:
    print('player earned 10 points')

#3.3
favorite_fruits = ['apple','grapes','pineapple']
if 'apple' in favorite_fruits:
    print('you must really like apples!')
if 'lychee' in favorite_fruits:
    print('you must really like lychee!')
if 'orange' in favorite_fruits:
    print('you must really like oranges!')

#3.4
age = 22
if age < 10:
    print('you are a kid')
elif age <20:
    print('you are a teen')
else:
    print('you are an adult')
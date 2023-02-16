'''
lab 5
'''
#3.1
alien_color= 'green'
if alien_color=='green':
    print('you just earned 5 points')
#3.2
alien_color= 'red'
if alien_color=='green':
    print('you just earned 5 points')
else:
    print('you just earned 10 points')
#3.3
favorite_fruits= ['mango','kiwi','watermelon']
if 'mango' in favorite_fruits:
    print('you love mango!')
if 'kiwi' in favorite_fruits:
    print('you like kiwis!')
if 'watermelon'in favorite_fruits:
    print('you like watermelon')
#3.4
age=19
if age<10:
    print('kid')
elif age>10 or age<20:
    print('teenager')
else:
    print('adult')
if age>65:
    print('elder')
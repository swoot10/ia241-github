'''
lec4
dict and tuple
'''

my_tuple = ('a', 'b', 'c', 'd', 'e')

print(type(my_tuple))
# if it were ('a') it wouldnt be a tuple but ('a',) would 
# my_tuple[0]='f'

# dictionary
my_car = {
        'color':'pink', 
        'maker':'toyota',
        'year':2015
}
print(my_car['year'])
print(my_car.items())
# color maker and year are keys  (.keys)
# pink toyota 2015 are values  (.values)
# items are the bunches of 2
print(my_car.get('color'))    #same as above
my_car['model'] = 'venza'  #adding in a new one to the existing dictionary
print(my_car)
my_car['year']=2020  #updating a value
print(my_car)

print(len(my_car))  #how value pairs in the dictionary
print('color' in my_car )   #will say true or false
print('pink' in my_car )  #will be false because its a value not a key
print('pink' in my_car.values() )  #will be true becuase we added the .values()
# to delete, my_car.pop('color')
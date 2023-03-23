'''
lec9
define class
'''
#to bring in a function from another file
import lec8

import numpy

print(numpy)

print(lec8.cal_plus(-9))
# return input

#class car:
#    maker = 'toyota'             #the maker of all the cars is toyota
#    
#    def report_maker(self):
#        
#        return self.maker
#        
#my_car_instance = car()
#print(my_car_instance.maker)
#print(my_car_instance.report_maker())  #does the same thing as above

#class car:
#    maker = 'toyota'
#    def __init__(self, input_model):
#        self.model = input_model
#my_car_instance = car('highlander')
#print(my_car_instance.maker)
#print(my_car_instance.model)  

#class car:
#    maker = 'toyota'
#    def __init__(self, input_model):
#        self.model = input_model
#my_camry = car('camry')
#print(my_camry.maker)
#print(my_camry.model)
#
#my_highlander = car('highlander')
#print(my_camry.maker)
#print(my_camry.model)

class car:
    maker = 'toyota'
    def __init__(self, input_model):
        self.model = input_model
    def report(self):
        return self.maker, self.model
        
my_camry = car('camry')
print(my_camry.maker)
print(my_camry.model)
print(my_camry.report())

my_camry.maker= 'Ford'
print(my_camry.report())
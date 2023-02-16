# import this 

# print( 1+15+
#              4564)
             
# 1 + 2 + \
# 12+ 

#a= [1,2,3]
#b= [1,2,3]
# not the same ids but the same values
#print(id(a))
#print(id(b))
#print(id([1,2,3]))

#print( a == b)

#print(a is b)
#a= 1
#b= 1
#same values and ids

# a=None

#print(id(a))
#print(id(None))

#print(a is None)
#print(a == None)

# x=[]   #empty list
# print(x is None)
#empty list is not considered None
#empty screen is not considered None
#same with set
#only None can be None

#boolean type
#print( True and False)
#print(True or False)
#print(not False)

# print(not '0')  will yield false
# print(not 0) will yield true

# if 2>1 : 
 #   print("2>1") #if you swtich the sign so its false, python wont run it
 #   print('another 2>1')
 #   if 3>1:   #nested if statement, if its wrong python wont run it
 #       print('3>1')
#else:                                       #applies to the 2>1 pair above because they are a pair with the same indentation
   # print('else statement')
    
#print('out of if block')
if 2<1:
    print('2>1')
    
elif 3>1:               #if the first one is wrong then it goes to the second(elif), if the first one is right it ignores the elif
    print('3>1')

else:
    print('else')
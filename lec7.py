'''
lec7
while loop
continue, break and pass
'''
#for/while loop
#for item in ['a', 'b']: #nested while loop
  #  print(item)
  #  i=5
   # while i>0:
    #    i= i-1   ##would just get 5 forever if we didn't put this here
     #   print(i)
        #
      #  if i==3:
       #     break   #breaks when it reached 3, entire while loop stopped bc we reached the break. didn't stop for loop, just while loop because while loop is smallest loop inside
#Continue statement
#i=5
#while i>0:
 #   i=i-1
  #  
   # if i==3:
    #    continue   #skips 3 and continues
    #
    #print(i)
#Pass statement
#i=5
#while i>0:
 #   i=i-1
  #  
   # if i==3:
    #    pass   
    #
    #print(i)
#exceptions
try:
    print(1/0)   #if there is an error, 'handle error2' will print, if there is no error, the code will print.
except:
    print('handle error2')
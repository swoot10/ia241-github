'''
lec6
for loop
range function
'''
# for num in [1,2,3]:
  #  print(num+1)
  #  print(num)
    
# for c in 'this is lec6':
 #   print(c)
#for c in 'this is lec6'.split():
 #   print(c)
    
# for num in [1,2,3]:
 #    if num >1:
     #    print(num)
#for word in 'this is lec6'.split():
  #  print(word)
  #  for c in word:
  #      print(c)
for i in range(1,5): 
    print(i)
    
num_list= [123,434,43234, 23423, 4234]

possible_max_num= num_list[0]

for num in num_list: 
    if num > possible_max_num:
        possible_max_num = num
        
print(possible_max_num)

#result, 0 when its addition, 1 when its multiplication
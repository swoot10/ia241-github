'''
lec3
lists and sets
'''

my_list=[1,2,3,4,5]

print(type(my_list))

my_nested_list= [1,2,3,my_list]
print(my_nested_list)

my_list[0]=6
print(my_list)

print(my_list[0])
# will give 6
print(my_list[1:3])
# will not include 3, beacuse it is the last value of the index
print(my_list[0:1])  #just the first one will be reported
print(my_list[:3])   #will assume that it starts at the 0th value of the list and will exclude the last value of the index
print(my_list[1:])  #will start with 1st value and list all others
x,y,z = ['a', 'b', 'c']       #assigns the items to each variable (ex. x=a)
print(x)

my_list.append(7)   #adds 7 to the end
print(my_list) 

my_list.remove(5)   #removes 5 from the list
print(my_list)

my_list.sort()  #puts them in order
print(my_list)

my_list.reverse()   #reverses the order, opposite as sort
print(my_list)

print(my_list + [8,9])   #combines two lists to add values

my_list.extend([8,9])
print(my_list)  #same thing as above

print( 2 in my_list)  #asking is there a 2 in my list? will yield a true or false
print('9' in my_list)  #will yield false because its a string

print(len(my_list))   #how many items in this list?

print(my_nested_list)
print(len(my_nested_list))

print('hello\tworld')   #tab
print('hello\nworld')   #new line

print(len('hello world'))   #how many characters in the script, spaces and periods count
print('hello world.'[0:5])  #will print the first 5 items

my_letters = ['a', 'a', 'b', 'b', 'c']
print(my_letters)
print(set(my_letters))  #unordered collection of distince problems
my_letters_set = set(my_letters)
print(my_letters_set)
print('a' in my_letters_set)   #will say true or false if a is in my letter set

print(list(my_letters_set)[0])


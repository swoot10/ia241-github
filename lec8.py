'''
lec 8
functions
'''

# def cal_plus(input1, input2):    #you could also say a and b instead of input or pretty much whatever
#    return input1 + input2
    
   # result= input1+input2
   # return result                alternative way to return
#print(cal_plus(1,3))
#print(cal_plus(2,7))


#def cal_plus(a, b):   
#    print(a)
#    print(b)
#    result=a+b
    
#    return result

#print(cal_plus(b=1, a=3))
#print(cal_plus(2,7))

#default value?
#def cal_plus(c, d=0):   
#    print(c)
#    print(d)
#    result=c+d
    
#    return result
#print(cal_plus(2))

# no value if there is no return statement
def cal_plus(c, d=0):   
    print(c)
    print(d)
    result=c+d
    
print(cal_plus(2))

#won't print the 1 becuase it's behind the return statement
#def cal_plus(a, b=0):  
#    return a+b
#    print(a)
#    print(b)
    
#print(cal_plus(2,1))

#absolute value function
#def cal_abs(a):
#    if a>0:
#        return a
#    else:
#        return -a
#print(cal_abs(-3))

#improved version of the past absval function
#def cal_abs(a):
    
#    if type(a) is str:
#        return ('wrong datatype')
    
#    elif a>0:
#        return a
#    else:
#        return -a
#print(cal_abs('0'))   #because it can't do zero/strings, we modified to return error

#ex2
#define a function to caluculate sigma
def cal_sigma(m,n):
    result=0
    for i in range(n, m+1):
        result= result + i
    return (result)   #this instead of print because we want a fruitful function
        
print(cal_sigma(10,1))

#define a function to calculate pi
def cal_pi(m,n):
    result=1
    for i in range(n,m+1):
        result=result*i
    return result

print(cal_pi(10,3))

#recursive function, real world try to avoid this.
def cal_f(m):
    if m==0:
        return 1
    else: 
        return m * cal_f(m-1)    #recursive aspect, function times itself    5 times factorial 4, 3, 2, 1, 0 and then it stops at 1. thats how we get 120 as a result
print(cal_f(5))

def cal_p(m,n):
    return cal_f(m)/cal_f(m-n)
print(cal_p(5,3))               #cal_f of 5 divided by cal_f of 5-3
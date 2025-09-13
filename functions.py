def greet():
    print('hello')
    print('welcome')

def addsub(x,y):
    c=x+y
    d=x-y
    return c,d

def mul(x,y):
    pass

greet()
result1,result2=addsub(9,10)
print(result1,result2)

#function argumenst
# def update(x):
#     x=8
#     print(x)
# a=10
# update(10)
# print(a)

def add(a,b):     #formal arguments
    c=a+b
    print(c)

add(7,3)    #actual arguments: position,keyword,default,variable length

def person(name,age):      #positional
    print(name)
    print(age)
#person()               #name and age are required arguments
def person(name='student',age=20):   #default arguments
    print(name)
    print(age)

person('sai',22)

person(name='kiran',age=22)   #keyword arguments

person('nikhil')    #takes default argument when age not mentioned

def sum(*b):    #variable length argument(tuple)
    print(b)
    c=0
    for i in b:
        c=c+i
    print(c)
sum(5,6,20,30,2.5)

def employee(name,**data)  :  #keyworded variable length argument
    print(name)                  #(dictionary)
    print(data)

employee('sai',age=20,id=123,city='goa')

#or

def name(**name):
    print("hello,",name['lname'],name['fname'])
name(fname='sai',lname='banoth')

#f-string
letter='hey my name is {} and i am from{}'
name='sai'
country='india'
print(letter.format(country,name))
print(f"hey my name is {name} and from {country}")


#docsstring
#written in function body just above function body or below function name
def square(n):
    '''hi this is square'''
    print(n**2)
square(4)
print(square.__doc__)
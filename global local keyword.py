a=10     #global variable
print(id(a))

def hello():
   #global a
    a=5        #local variable
    x=globals()['a']    #all the global variables 
    print(id(x))
    print(x)
    print('local a is',a)
    globals()['a']=20       #to modify global inside a functin
hello()
print(a)

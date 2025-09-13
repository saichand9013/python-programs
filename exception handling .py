a=5
b=1

try:
    print('resource open')
    print(a/b)
    k=int(input('enter the number'))
    print(k)
except ZeroDivisionError as e:                          #even the exception gets printed with message
    print('you cannot divide a number by zero',e)
except ValueError as e:
    print('invalid input',e)
except Exception as e:
    print('something went wrong')

finally:
    print('resource closed')





# #finally
# def fun1():
#     try:
#         l=[1,2,3,4]
#         i=int(input('enter the index:'))
#         print(l[i])
#     except:
#         print('some error occured')
#
#     finally:
#         print('i am always executed')
#
# x=fun1()
# print(x)
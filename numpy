from numpy import *


#ways of creating array in numpy
arr = array([1,2,3,4,5.0],int)
print(arr.dtype)
print(arr)

#linspace()    divides in number of parts
arr1=linspace(0,15,20)
print(arr1)

arr2=arange(1,15,2)   #here it is difference between nos
print(arr2)

arr3=logspace(1,40)
print(arr)

arr4=zeros(5)   #creats array with zeros of length 5
print(arr4)

arr5=ones(4)    #prints array of ones of length 4
print(arr5)

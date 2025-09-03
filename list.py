nums=[2,6,2,4,65,33,567,4]
print(nums)
print(nums[2])
print(nums[2::2])

nums2=[5,'sai',2.2]
print(nums)

print(nums+nums2)

#operations
nums.append(66)  #adds element at the end
nums.insert(2,22)   #adds element at specified index
nums.remove(6)    #remove by element
nums.pop(2)   #remove by index number
nums.pop()    #removes last element when index not specified
del nums[2:]   #deletes some elements that specified
nums.extend([2,34,675])   #adds few elemets at end
min(nums)    #finds the min in the list
max(nums)    #finds max num in the list
sum(nums)    #finds the sum of elements
nums.sort()  #sorts the list in order ascending
nums.sort(reverse=True)   #sort in descending order
nums.reverse()    #reverse the list
nums.index(2)   #returns the 1st occuring 2 elements index
nums.count(2)   # counts the no of occurings of element
no=nums.copy()  #copies the element nums and no are not linked
#if nums=no  then they are linked if we change no nums also changes
print(nums)
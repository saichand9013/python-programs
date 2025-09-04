set1={2,5,3,5}
set2={5,34,6,2,6}

print(set1)


#set methods
set1.union(set2)  #prints all elemnts and common elements once
set1.update(set2)   #set1 gets updated and set 2 elemets are added in set1

set1.intersection(set2)  #prints only the common elements once
set1.symmetric_difference(set2)  #print by removing common elemnts
set1.difference(set2)    #prints elements which are only present in set1
set1.issubset(set2)     #whether all elemnts of set 1 are there in set2
set1.issuperset(set2)
set1.add(8)     #adds element
set1.remove(3)   #removes the element
set1.discard(78)  #dosent throw error if element not present
del set1         #deleted the entire set
set1.clear()     #deleted the elements not set
set1.pop()      #removes a element from the set
print(set1)

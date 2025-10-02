#level2-t5
#task- filemanupulation
file = open('C:/Users/Sai/OneDrive/Desktop/cognizify/level 2/computers.txt','r')
data = file.read()
print("Given text file data is:",data)

occurrences = data.count('word')
print("Number of occurrences of the word :",occurrences)
occurrences = data.count('programming')
print("Number of occurrences of the word :",occurrences)
occurrences = data.count('computers')
print("Number of occurrences of the word :",occurrences)

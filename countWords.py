#! /usr/bin/env python3

import os
from buff import BufferedFdReader

# seeing space as done and doesn't finish -FIX THIS
def readWord(fd): #will return word
    word = ""
    completeWord = False 
    count = 0#check if a new line
    
    while(not completeWord):
        bytesRead = os.read(fd, 1)#reads a byte at a time

        if(len(bytesRead) == 0):#check if it read nothing
            return word
        charRead = bytesRead.decode() #decode byte to string

        if(charRead.isalpha()): #checks if its a letter
            #add to word
            word = word + charRead
        elif(charRead == " "):#encountered a space
            if(len(word) > 0):#already has read a full word
                completeWord = True
            else:
                #just a space
                continue
        elif(charRead == "\n"):#this doesn't work as it only reads 1 byte
            completeWord = True
        else:#other symbols
            completeWord = True

    return word.lower() #makes everything lowercase
#empty dictionary to keep track of number of a word
# word : n
dict = {}

#file descriptor
fd = os.open("declaration.txt", os.O_RDWR)

fileAble = True #to start while loop

#read contents of file and add to dictionary
while(fileAble):
    word = readWord(fd)#calls function
    #print(word)
    if(len(word) == 0):#checks if its the end of file
        #fileAble = False
        break
    #check uppercase WHEN == when
    #if word IS in dict increment n by 1
    if(word == " "):
        #do nothing
        continue
    elif(word in dict.keys()):
        dict[word] = dict[word] + 1
        #if word NOT in dict add to dict with n as 1
    else:
        dict[word] = 1


#close file
os.close(fd)

#print(dict)

#sort dictionary
dictKeys = list(dict.keys())
dictKeys.sort()
sortedDict = {i: dict[i] for i in dictKeys}

#write dictionary to an output file
fd = os.open("output.txt", os.O_RDWR | os.O_CREAT) #create new file
for word in sortedDict:
    #one word by line
    line = str.encode(word + " " + str(sortedDict[word])+ "\n")
    #print(line)
    os.write(fd, line)

os.close(fd)


#! /usr/bin/env python3

import os
import re
import string

from buff import BufferedFdReader

filename = 'declaration.txt'
fd = os.open(filename, os.O_RDONLY)

buffered_reader = BufferedFdReader(fd);

word_count = {}

try:
    while True:
        chunk = b""
        while True:
            byte = buffered_reader.readByte()
        
            if byte is None:
                break
            
            chunk += bytes([byte])
        if not chunk:
            break

        words = re.findall(r'\b\w+\b', chunk.decode())#split into words
        
        for word in words:
            
            word = word.strip(string.punctuation)#remove symbols
            
            if word: #check if there is a remaining word
                word = word.lower()
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
finally:
    buffered_reader.close();

dictKeys = list(word_count.keys())
dictKeys.sort()
sortedDict = {i: word_count[i] for i in dictKeys}

#write dictionary to an output file
fd = os.open("output.txt", os.O_RDWR | os.O_CREAT) #create new file
for word in sortedDict:
    #one word by line
    line = str.encode(word + " " + str(sortedDict[word])+ "\n")
    #print(line)
    os.write(fd, line)

os.close(fd)
    
                

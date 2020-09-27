#!/usr/bin/python
import os
# Check the file is present or not
fileLocation = input("Ener full path of file: ")
print ("Checking for ", fileLocation)
isPresent = os.path.exists(fileLocation)
if isPresent == True:
    print ("file is presnt")
    print ("+++++++++++++++++++++++++++++++++++++++++\n")
    searchstring = 'This is for interview'
    flag = 0
    fileread = open(fileLocation,'r+')
    content = fileread.read()
    print (content)
    fileread.close()
    filesearch = open(fileLocation,'r')
    for line in filesearch:
        if searchstring in line:
            flag +=1
    if flag == 0:
        print ("+++++++++++++++++++++++++++++++++++++++++\n")
        print ("'%s' not found in File" %(searchstring))
        print ("+++++++++++++++++++++++++++++++++++++++++\n")
        exit()
    else:
        print ("+++++++++++++++++++++++++++++++++++++++++\n")
        print("'%s' found %d times in File '%s'"%(searchstring,flag,fileLocation))
        filesearch.close()
    print ("+++++++++++++++++++++++++++++++++++++++++\n")
    print("Replacing '%s' with '%s'"%(searchstring,searchstring.upper()))
    content = content.replace(searchstring,searchstring.upper())
    filereplace = open(fileLocation,'w')
    filereplace.write(content)
    print ("+++++++++++++++++++++++++++++++++++++++++\n")
    print (content)
    print ("+++++++++++++++++++++++++++++++++++++++++\n")
    filereplace.close()
else:
    print ("File does not exist")
    print ("+++++++++++++++++++++++++++++++++++++++++\n")
    exit()

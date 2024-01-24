import os
import os.path

#os.mkdir('crtdFolder')
names = os.listdir('.') #current directory
print(names)

x = os.path.exists('myfile.txt')
print(f'the existance of myfile.txt is: {x}')

# remove a folder
#os.rmdir('crtdFolder')


# remove a file
os.remove('myfile.txt')
a = os.listdir('.')
print(a)

"""
# make file ready for reading by opening it
file = open('/home/oray/Documents/Projects/Scientific computing with Python/String manipulation/myfile.txt','r')
file = open('/home/oray/Documents/Projects/Scientific computing with Python/String manipulation/myfile.txt','a')
# read all contents of file using read()
content = file.read()
# open file in write mode, to overide contents

file.write("I am th creator of this file...")
print(f'file contents:\n{content}')
# read a line from a file
line = file.readline()
print(f'line: {line}')
# read lines and return a list of lines from file
lines = file.readlines()
print(f'lines: {lines}')
# close the file after reading
file.close()
file.close()

"""
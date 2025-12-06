#-----------Old traditional way
file = open('alpha.txt', 'r') #The default permission is also 'r'

content= file.read()
print(content)
file.close() #Closing the file. Each time open a file, close it

#--------------------------------------------------------------------------------------------
# While we can use the above method to do file handling, it's not the best practice
# We can use something called context manager which comes with -> with open()... method

with open('alpha.txt') as file2:
    content= file2.read() #Read the whole thing at once
    print(len(content))

with open('alpha.txt') as file3:
    #--------------Cannot execute both read() & readlines() at once
    lines= file3.readlines() #Read the file line by line
    for line in lines:
        print(line)
        
#--------Reading a single line only
with open('alpha.txt', 'r') as file4:
    single_line1= file4.readline()
    single_line2= file4.readline()
    print(single_line1)
    print(single_line2)

#---------Reading only a certain amount of cahracters
read_amount= 15
with open('alpha.txt') as file5:
    content1= file5.read(read_amount)
    content2= file5.read(read_amount)
    print(content1)
    print(content2)

#Reading a file with a predetermined character amount block by block
def getLen(x):
    with open(x) as f:
        content = f.read()
        content_len= len(content)
        return content_len

with open('alpha.txt', 'r') as file6:    
    content_len= getLen('alpha.txt')
    reps= round(content_len/read_amount)
    for i in range (0,reps):
        print(file6.read(read_amount))

#The same thing above can be achieved with "seek" method        
with open('alpha.txt') as file7:
    content= file7.read()
    content_len= len(content)
    reps= round(content_len/read_amount)
    file7.seek(0) #Pointing back that you have to go to first starting point again
    for i in range (0,reps):
        print(file7.read(read_amount))

#-----Reading multiple files using OS library
import os

files= os.listdir(os.curdir) #curdir can find the current directory we are in
for file in files:
    if file.endswith('.txt'):
        with open(file, 'r') as f:
            content= f.read()
            print(content)

#-------Writing Files
with open('newFile.txt', 'w') as fn:
    fn.write("First line of text with Python file handling")

#-------Adding text to existing files
with open('alpha.txt', 'a') as ff:
    ff.write("\n")
    ff.write("5) Fifth tip is thr worsst tippp")

#-----------Challenge-------------
def writeNewTip(index, msg):
    with open('alpha.txt', 'a') as fnn:
        fnn.write("\n")
        fnn.write(f"{index}) {msg}")

with open('alpha.txt', 'r') as fff:
    lines= fff.readlines()
    new_index= (len(lines) -  5) + 1
    message= "Seventh time I'm telling you!"

    writeNewTip(new_index, message)

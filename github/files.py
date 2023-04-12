###################################################
# files
###################################################
import os

def readFileStr():
    print('=========== read a file into a string ===========')
    f = open('file.txt')
    data = f.read()
    print(data, type(data))
    rdata = open('file.txt').read()
    print(rdata)
    print(dir(f)) #To get help on any object
    f.close() # Close to flush output buffers to disk

def writeFile():
    print('=========== write into a file ===========')
    f = open('file.txt', 'w') # Make a new file in output mode
    f.write('adding more\n') # Write strings of bytes to it
    f.write('lines ')
    f.close()         # Close to flush output buffers to disk

def appendFile():
    print('=========== write append and read using with statement ===========')
    with open("myfile.txt", "w") as file1:
        file1.write('Hello \n')
        L = ["This is hello ", "John ", "World"]
        file1.writelines(L)
    with open("myfile.txt", 'a') as file1:
        file1.write(" Today")
    with open("myfile.txt", "r+") as file1:
        # Reading form a file
        print(file1.read())        

def readFileLine():
    print('=========== read a file line by line ===========================')
    lines = [line.rstrip() for line in open('file.txt')] 
    print(lines)
    #rstrip preserves white space chars at beginning and end of each line
    lines = [line.strip() for line in open('file.txt')] #got all file contents in lines
    #strip removes white space chars at beginning and end of each line
    print(lines, type(lines))

def createDeleteFile():
    print('=========== create and remove a file ===========================')
    f = open('newfile.txt', 'w')
    f.write('Hello world john')
    f = open('newfile.txt', 'r')
    print(f.read())
    f.close()
    os.remove('newfile.txt')

if __name__ == '__main__':
    readFileStr()
    writeFile()
    appendFile()
    readFileLine()
    createDeleteFile()
import datetime
import time
import sys

validFile = False
file = raw_input('File >')

if file[-4:] == '.jel':
    validFile = True
else:
    sys.exit('Invaild File')

done = False
error = ''
contents = []
builtins = ['terminal', 'file']

with open(file, 'r') as myfile:
    content = myfile.read().replace('\n', '')

contents = [part + ';' for part in content[:-1].split(';')]

line = 0
command = ''

def returnCommand(c):
    num = 0
    builtinNum = None
    while num <= len(builtins):
        if builtins[num] in c:
            builtinNum = num
        else:
            num = num + 1
    builtinsFound = False
    if builtinsFound:
        index = 0
        current = ''
        dotFound = False
        commandFound = False
        command = ''
        Adone = False
        while not Adone:
            if index > len(c):
                Adone = True
            elif c[index - 1] == '.':
                dotFound = True
                current = current
            elif dotFound:
                command = command + c[index - 1]
            index = index + 1
        command = command[:-1]
        return command

def returnLibrary(c):
    num = 0
    builtinNum = None
    while num <= len(builtins):
        if builtins[num] in c:
            builtinNum = num
        else:
            num = num + 1
    builtinsFound = False
    if builtinsFound:
        index = 0
        current = ''
        dotFound = False
        commandFound = False
        command = ''
        Adone = False
        while not Adone:
            if index > len(c):
                Adone = True
            elif c[index - 1] == '.':
                dotFound = True
                current = current
            elif dotFound:
                command = command + c[index - 1]
            index = index + 1
        command = command[:-1]
        return current
print returnLibrary(contents[2])
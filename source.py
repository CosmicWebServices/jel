import datetime
import time

file = 'example.jel'
done = False
error = ''
contents = []
builtins = ['terminal', 'file']

with open(file, 'r') as myfile:
    content = myfile.read().replace('\n', '')

contents = [part + ';' for part in content[:-1].split(';')]

line = 0
print contents

def readCommand(c):
    if builtins[0] or builtins[1] in c:
        index = 0
        current = ''
        dotFound = False
        commandFound = False
        command = ''
        Adone = False
        while not Adone:
            if index > len(c):
                Adone = True
            elif c[index] == '.':
                dotFound = True
                current = current
            elif dotFound:
                command = current + c[index]
            index = index + 1

readCommand(contents[1])
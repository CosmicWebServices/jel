#!/usr/bin/python
import datetime
import time
import sys
import subprocess
import argparse
import codecs

parser = argparse.ArgumentParser(description='')
validFile = False
file = sys.argv[1]

if file[-4:] == '.jel':
    validFile = True
    print 'File Vaildated'
elif not validFile:
    sys.exit('Invaild File')


done = False
error = ''
contents = []
builtins = ['terminal', 'file']

with open(file, 'r') as myfile:
    content = myfile.read().replace('\n', '')

print 'Retrieved File Contents'

contents = [part + ';' for part in content[:-1].split(';')]

print 'File Splitted'

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
def wc(filename):
    """
    counts # of lines in a file (Like UNIX's [wc -l])
    """
    with codecs.open(filename, 'r') as f:
        lc = sum(1 for l in f)
    return lc
wc('jel')
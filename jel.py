#!/usr/bin/python
import datetime
import time
import sys
import subprocess
import argparse
import codecs

parser = argparse.ArgumentParser(description='')
validFile = False
arg = sys.argv[1]
version = '1.0.1'

if arg[-4:] == '.jel':
    validFile = True
    print 'File Vaildated'
elif arg == '-help':
    print 'The following commands are all run with jel'
    print ''
    print '<filename>   Runs the Jel parser on a file with a .jel extension'
    print '-version   Returns the version of Jel you are using'
    print '-update   Updates to the newest version of Jel'
    print '-help   Returns the jel help screen'
    sys.exit()
elif arg == '-version':
    print version
    sys.exit()
elif arg == '-update':
    subprocess.call('npm', 'install', '-g', 'jel')
if not validFile:
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
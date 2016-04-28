#!/usr/bin/python
import datetime
import time
import sys
import subprocess
import argparse

validFile = False
arg = sys.argv[1]
version = '1.0.2'

if arg[-4:] == '.jel':
    validFile = True
    print 'jel: file extension validated'
elif arg == '-help':
    print 'The following commands are all run with jel'
    print ''
    print '<filename>   Runs the Jel parser on a file with a .jel extension'
    print '-version   Returns the version of Jel you are using'
    print '-help   Returns the jel help screen'
    sys.exit()
elif arg == '-version':
    print version
    sys.exit()
if not validFile:
    sys.exit('Invaild File')


done = False
error = ''
contents = []
builtins = ['terminal', 'file']

with open(arg, 'r') as myfile:
    content = myfile.read().replace('\n', '')

print 'jel: retrieved file contents'

contents = [part + ';' for part in content[:-1].split(';')]

print 'jel: file splitted'

line = 0
command = ''
#!/usr/bin/python
import datetime
import time
import sys
import subprocess
import argparse

validFile = False
arg = sys.argv[1]
version = '1.0.3'

if arg[-4:] == '.jel':
    validFile = True
    print 'jel: \033[92mfile extension validated\033[0m'
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
    sys.exit('jel: \033[91minvalid file\033[0m')


done = False
error = ''
contents = []
builtins = ['terminal', 'file']

with open(arg, 'r') as myfile:
    content = myfile.read().replace('\n', '')

print 'jel: \033[92mretrieved file contents\033[0m'

contents = [part + ';' for part in content[:-1].split(';')]

print 'jel: \033[92mfile splitted\033[0m'

line = 0
command = ''
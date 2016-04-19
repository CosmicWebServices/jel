import datetime
import time
from jelscript.commands.file import getContents

file = 'example.jel'
done = False
error = ''
contents = []

with open(file, 'r') as myfile:
    content = myfile.read().replace('\n', '')

contents = [part + ';' for part in content[:-1].split(';')]

line = 0
test = getContents('example.jel')
print test
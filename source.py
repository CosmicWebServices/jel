import datetime
import time

file = 'example.baran'
done = False
error = ''
contents = []

with open(file, 'r') as myfile:
    content = myfile.read().replace('\n', '')

print content

contents = [part + ';' for part in content[:-1].split(';')]
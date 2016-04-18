import datetime
import time

file = 'example.jel'
done = False
error = ''
contents = []

with open(file, 'r') as myfile:
    content = myfile.read().replace('\n', '')

contents = [part + ';' for part in content[:-1].split(';')]

print contents
import datetime
file = 'example.barn'
done = False
error = ''

with open(file, 'r') as myfile:
    contents = myfile.read().replace('\n', '')

contents = []
# Functions
today = ['.date', '.year', '.hour', '.minute', '.second']
terminal = ['.write', '.run', '.input']
file = ['.getContents', '.length']
def split(file):
    lengthOfFile = len(file)
    endFound = False
    fileIndex = 0
    current = ''
    while endFound == False:
        if file[fileIndex] == ';':
            current = current + ';'
            contents.append(current)
            if fileIndex == lengthOfFile:
                endFound = True
        else:
            current = current + file[fileIndex]
        fileIndex = fileIndex + 1
    print contents

split(file)
print contents
import datetime
file = 'example.ba'
done = False
error = ''
contents = []
with open(file, 'r') as myfile:
    content = myfile.read().replace('\n', '')


# Functions
today = ['.date', '.year', '.hour', '.minute', '.second']
terminal = ['.write', '.run', '.input']
file = ['.getContents', '.length']
# End
print content
def splitFile(file):
    lengthOfFile = len(file)
    endFound = False
    fileIndex = 0
    current = ''
    while not endFound:
        if file[fileIndex] == ';':
            current = current + ';'
            contents.append(current)
            if fileIndex == lengthOfFile:
                endFound = True
        else:
            current = current + file[fileIndex]
        fileIndex = fileIndex + 1
splitFile(content)
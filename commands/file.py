def getContents(file):
    with open(file, 'r') as myfile:
        return myfile.read().replace('\n', '')
        
def length(file):
    with open(file, 'r') as myfile:
        content = myfile.read().replace('\n', '')
        return len(content)
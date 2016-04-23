import subprocess
    
def run(command):
    subprocess.call(command, shell=True)

def input(content):
    raw_input(content)

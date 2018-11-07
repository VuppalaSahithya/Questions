# Write a program to find and replace string/pattern in a file and replace the file with the updated string

with open('input.txt','r') as f:
    newlines = []
    for line in f.readlines():
        newlines.append(line.replace('One', 'Test'))
with open('input.txt', 'w') as f:
    for line in newlines:
        f.write(line)
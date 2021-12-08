input="Challenge2Input.txt"

position=0
depth=0

with open(input, 'r') as file:
    lines=file.readlines()
    for line in lines:
        line=line.strip().split()
        if line[0][0]=='f':
            position+=int(line[1])
        elif line[0][0]=='d':
            depth+=int(line[1])
        else:
            depth-=int(line[1])

print(position*depth)

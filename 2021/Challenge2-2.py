input="Challenge2Input.txt"

position=0
depth=0
aim=0

with open(input, 'r') as file:
    lines=file.readlines()
    for line in lines:
        line=line.strip().split()
        if line[0][0]=='d':
            aim+=int(line[1])
        elif line[0][0]=='u':
            aim-=int(line[1])
        else:
            position+=int(line[1])
            depth+=(aim*int(line[1]))

print(position*depth)

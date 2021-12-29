input="Challenge8Input.txt"

total=0

with open(input,'r') as file:
    data=file.readlines()
    for line in data:
        outputs=line.strip().split(' | ')[1].split()
        for output in outputs:
            if len(output)==2 or len(output)==3 or len(output)==4 or len(output)==7:
                total+=1

print(total)

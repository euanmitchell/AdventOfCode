input="Challenge3Input.txt"

data=[]

with open(input,'r') as file:
    lines=file.readlines()
    for line in lines:
        data.append(line.strip())

index=0
def greater(input, index):
    listZero=[]
    listOne=[]
    for item in input:
        if item[index]=='0':
            listZero.append(item)
        else:
            listOne.append(item)
    if len(listZero) > len(listOne):
        if len(listZero) > 1:
            greater(listZero,index+1)
        else:
            print(int(listZero[0],2))
    else:
        if len(listOne) > 1:
            greater(listOne,index+1)
        else:
            print(int(listOne[0],2))

def lesser(input, index):
    listZero=[]
    listOne=[]
    for item in input:
        if item[index]=='0':
            listZero.append(item)
        else:
            listOne.append(item)
    if len(listZero) <= len(listOne):
        if len(listZero) > 1:
            lesser(listZero,index+1)
        else:
            print(int(listZero[0],2))
    else:
        if len(listOne) > 1:
            lesser(listOne,index+1)
        else:
            print(int(listOne[0],2))

oxygenRating=greater(data,index)
scrubberRating=lesser(data,index)

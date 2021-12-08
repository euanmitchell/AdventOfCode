import numpy as np

input="Challenge6Input.txt"

with open(input,'r') as file:
    data=file.readline()
    data=data.strip().split(',')

#data=['3','4','3','1','2']

totals=[0,0,0,0,0,0,0,0,0]

for item in data:
    totals[int(item)]+=1

print('Initial state:',totals)

def increment(input,days):
    output=[0,0,0,0,0,0,0,0,0]
    output[0]=input[1]
    output[1]=input[2]
    output[2]=input[3]
    output[3]=input[4]
    output[4]=input[5]
    output[5]=input[6]
    output[6]=input[0]+input[7]
    output[7]=input[8]
    output[8]=input[0]
    if days==256:
        print('Day {}: {}'.format(days,output))
        result=np.array(output)
        print(np.sum(result))
    else:
        print('Day {}: {}'.format(days,output))
        increment(output,days+1)

increment(totals,1)

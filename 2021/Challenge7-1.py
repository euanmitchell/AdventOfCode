import numpy as np

input="Challenge7Input.txt"

with open(input,'r') as file:
    data=file.readline()
    data=data.strip().split(',')

arrayData=np.array(data,dtype=np.int)
print('Minimum:',min(arrayData))
print('Maximum:',max(arrayData))

positions=np.full((max(arrayData)),0)
print(positions.shape)

for i in range(positions.shape[0]):
    diffs=arrayData-i
    diffs=np.absolute(diffs)
    sum=np.sum(diffs)
    positions[i]=sum

print(np.min(positions))

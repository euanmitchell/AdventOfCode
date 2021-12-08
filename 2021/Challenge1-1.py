import numpy as np

input="Challenge1Input.txt"

data=np.loadtxt(input)
counter=0
for i in range(data.shape[0]-1):
    diff=data[i+1]-data[i]
    if diff>0:
        counter+=1
print(counter)

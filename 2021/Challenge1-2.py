import numpy as np

input="Challenge1Input.txt"

data=np.loadtxt(input)
counter=0
for i in range(data.shape[0]-3):
    window1Sum=np.sum(data[i:i+3])
    window2Sum=np.sum(data[i+1:i+4])
    diff=window2Sum-window1Sum
    if diff>0:
        counter+=1
print(counter)

import numpy as np

input="Challenge6Input.txt"

with open(input,'r') as file:
    data=file.readline()
    data=data.strip().split(',')

#data=['3','4','3','1','2']
print('Initial state:',data)

totals=[]

for i in range(81):
    def spawn(input,counter):
        if counter>=i:
            totals.append((len(input)))

        else:
            output=[]
            for index, item in enumerate(input):
                if item==0:
                    output.append(6)
                    output.append(8)
                else:
                    output.append(int(item)-1)
            #print('After {0} days: {1}'.format(counter,output))
            spawn(output,counter+1)

    spawn(data,1)

import numpy as np

input="Challenge3Input.txt"

with open(input,'r') as data:
    line=data.readline()
    columns=len(line.strip())

totals=np.zeros(columns,dtype=np.int)
gamma=np.zeros(columns,dtype='str')
epsilon=np.zeros(columns,dtype='str')
counter=0

with open(input,'r') as data:
    lines=data.readlines()
    for line in lines:
        line=line.strip()
        for i in range(len(line)):
            totals[i]+=int(line[i])
        counter+=1

half=counter/2

for i in range(totals.shape[0]):
    if totals[i]>half:
        gamma[i]='1'
        epsilon[i]='0'
    else:
        gamma[i]='0'
        epsilon[i]='1'

gammaDec=''
epsilonDec=''
for i in range(totals.shape[0]):
    gammaDec+=str(gamma[i])
    epsilonDec+=str(epsilon[i])

print(int(gammaDec,2))
print(int(epsilonDec,2))

print(int(gammaDec,2)*int(epsilonDec,2))

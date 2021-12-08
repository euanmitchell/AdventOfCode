import numpy as np

input="Challenge4Input.txt"

with open(input,'r') as file:
    line=file.readline()
    numbers=line.strip().split(',')

boards=np.loadtxt(input,skiprows=1,comments='\n',dtype=np.int)
boards=np.reshape(boards,(-1,5,5))
boards=np.insert(boards,boards.shape[1],0,axis=1)
boards=np.insert(boards,boards.shape[2],0,axis=2)
# shape[0]=boards
# shape[1]=rows
# shape[2]=columns
print(boards.shape)

# Loop through each number to be played
for number in numbers:
    number=int(number)
    boards[boards==number]=100

    # Loop through each game board
    for i in range(100):
        # Loopthrough each row and column
        for j in range(5):
            boards[i,j,5]=np.sum(boards[i,j,:5])
            boards[i,5,j]=np.sum(boards[i,:5,j])
    stop=np.where((boards[:,5,5]==500))
    if len(stop[0])>0:
        winningBoard=i
        break
print('Winning board',winningBoard)

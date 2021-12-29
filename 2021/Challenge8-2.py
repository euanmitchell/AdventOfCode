input="Challenge8Input.txt"

total=0

with open(input,'r') as file:
    # Get each individual line
    data=file.readlines()
    for line in data:
        mapping={'t':'', 'm':'', 'b':'', 'tl':'', 'tr':'', 'bl':'', 'br':''}
        letters={'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0}

        # Get the ten input strings in a list
        inputs=line.strip().split(' | ')[0].split()
        # Get single list of all the input values and update letters dict
        bitList=[]
        for input in inputs:
            bits=(list(map(str,input)))
            for bit in bits:
                letters[bit]+=1
                bitList.append(bit)

        # Update mapping dict with the unique occurrences - gives us three
        mapping['bl']=list(letters.keys())[list(letters.values()).index(4)]
        mapping['tl']=list(letters.keys())[list(letters.values()).index(6)]
        mapping['br']=list(letters.keys())[list(letters.values()).index(9)]

        # Use features of ones, fours, and sevens to get three more
        for input in inputs:
            if len(input)==2:
                one=list(map(str,input))
            if len(input)==3:
                seven=list(map(str,input))
            if len(input)==4:
                four=list(map(str,input))
        current=mapping.values()
        for digit in one:
            if digit not in current:
                mapping['tr']=digit
        current=mapping.values()
        for digit in seven:
            if digit not in current:
                mapping['t']=digit
        current=mapping.values()
        for digit in four:
            if digit not in current:
                mapping['m']=digit

        # Only one letter left
        current=mapping.values()
        for letter in letters.keys():
            if letter not in current:
                mapping['b']=letter

        # Define the 10 digits as strings?
        zero=[mapping['t'],mapping['tl'],mapping['bl'],mapping['b'],mapping['br'],mapping['tr']]
        one=[mapping['br'],mapping['tr']]
        two=[mapping['t'],mapping['bl'],mapping['b'],mapping['tr'],mapping['m']]
        three=[mapping['t'],mapping['b'],mapping['br'],mapping['tr'],mapping['m']]
        four=[mapping['tl'],mapping['br'],mapping['tr'],mapping['m']]
        five=[mapping['t'],mapping['tl'],mapping['b'],mapping['br'],mapping['m']]
        six=[mapping['t'],mapping['tl'],mapping['bl'],mapping['b'],mapping['br'],mapping['m']]
        seven=[mapping['t'],mapping['br'],mapping['tr']]
        eight=[mapping['t'],mapping['tl'],mapping['bl'],mapping['b'],mapping['br'],mapping['tr'],mapping['m']]
        nine=[mapping['t'],mapping['tl'],mapping['b'],mapping['br'],mapping['tr'],mapping['m']]
        numbers=[zero,one,two,three,four,five,six,seven,eight,nine]

        # Get the four output strings in a list
        outputs=line.strip().split(' | ')[1].split()
        result=''
        for output in outputs:
            output=list(map(str,output))
            output.sort()
            for index,number in enumerate(numbers):
                number.sort()
                if output==number:
                    result+=str(index)
        total+=int(result)

print(total)

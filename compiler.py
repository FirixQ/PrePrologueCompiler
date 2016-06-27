#prologue thing

#fileLocation = input('File location: ')
fileLocation = 'script.pre'
f = open(fileLocation) #input file

o = open(fileLocation + '.pl', 'w') #output file

o.write('/* Compiled from PrePrologue to Prologue by PPC */\n')

for line in f:
    if (line[0] == '/'):
        #skip line
        #print(line)
        o.write(line + '\n')
        something = 'thing'
    elif(line[0] == '\n'):
        #skip line
        something = 'nothing'
    elif(line[0] == '!'):
        line = line[1:]
        parts = line.split('{')
        factName = parts[0]
        values = parts[1].replace('}', '')
        values = values.replace(' ', '')
        values = values.replace('\n', '')
        values = values.split(',')
        for item in values:
            toWrite = factName + '(' + item + ').'
            o.write(toWrite + '\n')
            #print(toWrite)

        o.write('\n')
        #print('')

    elif(line[0] == '?'):
        toWrite = line[1:]
        #print(toWrite)
        o.write(toWrite)
            

f.close()
o.close()
print('Finished')

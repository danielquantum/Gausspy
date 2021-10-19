"""
Spyder Editor

Creating gzmt format from zmatrix (variables) gaussian
"""
###########################################
# Input and Output files
###########################################
item='gzmt.txt'
item1='variables.txt'
out='Coord.gzmt'

file_in1 = open(item1,'r')
file_in_lines1 = file_in1.readlines()
file_in = open(item,'r')
file_out = open(out, 'w+')
file_in_lines = file_in.readlines()

###########################################
# Creating a dictionary of variables
###########################################
list_keys = []
list_values = []
#n=0
for line in (file_in_lines1): 
    linesplit = line.split()
    #print(linesplit)
    list_keys.append(linesplit[0])
    list_values.append(linesplit[1])
    #n += 1
    #if n == 3:
        #break

file_in1.close()
#print(list_keys)
#print(list_values)
D = dict(zip(list_keys,list_values))
#print(D)

###########################################
# Creating a gzmt format
###########################################
n=0
#Tabulating Lines
pList = []
for i, line in enumerate(file_in_lines):  
    list_words = []
    linesplit = line.split()
    #print(linesplit)
    #print(len(linesplit))
    ###########################################
    if i > 0:
        BondI = linesplit[2]
        #BI = D.[]
        #print(BondI)
    if i > 1:
        AngleI = linesplit[4]
        #print(AngleI)
    if i > 2:
        DihedralI = linesplit[6]
        #print(DihedralI)
    ###########################################
    if len(linesplit) == 1:
        pList.append(linesplit)
    if len(linesplit) == 3:
        list_words.append(linesplit[0])
        list_words.append(linesplit[1])
        list_words.append(D[BondI])
        pList.append(list_words)
    if len(linesplit) == 5:
        list_words.append(linesplit[0])
        list_words.append(linesplit[1])
        list_words.append(D[BondI])
        list_words.append(linesplit[3])
        list_words.append(D[AngleI])
        pList.append(list_words)
    if len(linesplit) == 8:
        list_words.append(linesplit[0])
        list_words.append(linesplit[1])
        list_words.append(D[BondI])
        list_words.append(linesplit[3])
        list_words.append(D[AngleI])
        list_words.append(linesplit[5])
        list_words.append(D[DihedralI])
        pList.append(list_words)
    #print(pList)
   # n += 1
   # if n == 4:
   #     break
    
file_in.close() 

# Write to file
for item in pList:
    #print(item)
    listToStr = ' '.join([str(element) for element in item])
    file_out.write(listToStr)
    file_out.write('\n')
    
file_out.close()
    

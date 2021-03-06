"""
Extract xyz files from geometry optimization calculations
"""
item='ClampBCl3.g16_16214721.log'
file_in = open(item,'r')
file_in_lines = file_in.readlines()

n = 0
list_lines = []
D = {'1':'H', '5':'B' ,'6':'C', '7':'N', '9':'F', '17':'Cl'}
for index, line in enumerate(file_in_lines):            
    if 'Standard orientation' in line:
        list_lines.append('38\n')
        list_lines.append('Comment\n')
        n = 1 # Sign of finding 'Standard Orientation'
    if n == 1 and '-----' in line:
        i = index
        n = 2 # Sign of finding First '---'
    if n == 2 and '-----' in line and index > i:
        n = 3 # Sign of finding Second '---'
        i = index
        m = 38 + 1
        mz = index + m 
    if n == 3 and index < mz:
        if '-----' not in line:
            i = index
            linesplit = line.split() #List
            atom = D[linesplit[1]]
            newline = atom + ' ' + linesplit[3] + ' ' + linesplit[4] + ' ' + linesplit[5] + '\n'
            list_lines.append(newline)
            m -= 1
        if '-----' in line and index > i:
            n = 0 # Sign of finding Third(last) '---'
print(list_lines)
file_in.close()


file_out = open('Opt_trj.xyz', 'w+')
# Write to file
for a in list_lines:
    #print(item)
    file_out.write(a)
    #file_out.write('\n')
    
file_out.close()

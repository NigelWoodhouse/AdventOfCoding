file = open('input.txt', 'r')
counter = 0
for line in file:
    compt1 = ''.join(sorted(set(line[len(line)//2:-1])))
    compt2 = ''.join(sorted(set(line[:len(line)//2])))
    common_char = list(set(compt1).intersection(compt2))[0]
    # compt1_index = 0
    # compt2_index = 0
    # while(compt1[compt1_index] != compt2[compt2_index]):
    #     if(compt1[compt1_index] < compt2[compt2_index]):
    #         compt1_index+=1
    #     else:
    #         compt2_index+=1
    # common_char = compt1[compt1_index]
    if common_char.islower():
        counter += ord(common_char)-96
    else:
        counter += ord(common_char)-38
print(counter) #7845
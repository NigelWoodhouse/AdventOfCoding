def compute(system):
    f = open('numbers.txt', 'r')
    content = f.readlines()

    num_numbers = len(content)
    len_num = len(content[0])-1

    list = []
    for j in range(len_num):
        
        count = 0
        for i in range(len(content)):
            count += int(content[i][j])
        MCN = system_binary(count, system, content)
        for i in range(len(content)):
            if content[i][j] == MCN:
                list.append(content[i])
        content = list
        list = [] 
        if len(content) == 1:
            print(content[0])
            return content[0]
        
    
def system_binary(count, system, content):
    if system == "O2":
        if count > len(content)/2:
            binary = "1"
        elif count < len(content)/2:
            binary = "0"
        else:
            binary = "1"
    if system == "CO2":
        if count > len(content)/2:
            binary = "0"
        elif count < len(content)/2:
            binary = "1"
        else:
            binary = "0"
    return binary

O2 = int(compute("O2"),2)
CO2 = int(compute("CO2"),2)   
print(O2*CO2)
file = open("input.txt", "r")
MAX_FILESIZE = 100000
directories = {}
path = ""
cur_dir = ""
for line in file:
    command = line.split()
    # Check for if cd or ls based on $
    if command[0] == "$":
        if command[1] == "cd":
            if command[2] == "..":
                path = path.rsplit(":",2)[0]+":"
            else: 
                path += command[2] + ":"
                if path not in directories:
                    directories[path] = 0           
        else: # ls gives list of directories and files
            continue
    # check for if dir or file
    else:
        if command[0] == "dir":
            continue
        else:
            ind_dir = path.split(":")[:-1]
            col_path = ""
            for i in range(len(ind_dir)):
                col_path += ind_dir[i] + ":"
                directories[col_path] += int(command[0])
            # print(directories)
filesizes = 0
for value in directories.values():
    if value <= MAX_FILESIZE: filesizes += value
print(filesizes)
# 1423358
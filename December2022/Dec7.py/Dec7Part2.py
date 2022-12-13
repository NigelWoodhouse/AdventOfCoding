file = open("input.txt", "r")
LIMIT_FILESIZE = 30000000
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
filesize_to_delete = directories["/:"]
remaining_space = 70000000 - directories["/:"]
for value in directories.values():
    if (value <= filesize_to_delete) and (value >= LIMIT_FILESIZE-remaining_space):
        filesize_to_delete = value
print(filesize_to_delete)
# 545729

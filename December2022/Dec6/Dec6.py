file = open("input.txt", "r")
line = file.readline()
marker_len = 4
character_bucket = []
print(character_bucket)
for index, char in enumerate(line):
    character_bucket.append(char)
    if len(character_bucket) >= marker_len+1:
        del character_bucket[0]
    if len(set(character_bucket)) == len(character_bucket) and len(character_bucket) == marker_len:
        print(index+1)
        break
# 1802
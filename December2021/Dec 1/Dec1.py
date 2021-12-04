f = open('numbers.txt', 'r')
content = f.read().split()

print(len(content))

inc_count = 0
dec_count = 0
same_count = 0
prev = 171

for i in range(len(content)):
    print(content[i])
    if int(content[i]) > prev:
        inc_count += 1
    elif int(content[i]) < prev:
        dec_count += 1
    else:
        same_count += 1
    prev = int(content[i])

print("Increased: %s Decreased: %s Same: %s" %(inc_count, dec_count, same_count))
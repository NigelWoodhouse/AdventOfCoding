f = open('numbers.txt', 'r')
content = f.read().split()

print(len(content))

inc_count = 0
dec_count = 0
same_count = 0
prev = 518

for i in range(len(content)-2):
    sum = int(content[i])+int(content[i+1])+int(content[i+2])
    print(sum)
    if sum > prev:
        inc_count += 1
    elif sum < prev:
        dec_count += 1
    else:
        same_count += 1
    prev = sum

print("Increased: %s Decreased: %s Same: %s" %(inc_count, dec_count, same_count))
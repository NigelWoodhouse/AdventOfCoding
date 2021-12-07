f = open("numbers.txt", "r")
crabs = f.readline().split(",")
crabs = list(map(int, crabs))

master_fuel = 1000000000 # a big number
for pos in range(max(crabs)+1):
    pos_fuel = 0
    for i in range(len(crabs)):
        pos_fuel += abs(crabs[i]-pos)*(abs(crabs[i]-pos)+1)/2
    if pos_fuel < master_fuel:
        master_fuel = pos_fuel
        master_pos = pos
       
print(int(master_pos))
print(int(master_fuel))
# 464, 98363777
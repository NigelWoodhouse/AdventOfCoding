import statistics

f = open("numbers.txt", "r")
crabs = f.readline().split(",")
crabs = list(map(int, crabs))

med = statistics.median(crabs)
fuel = 0
for i in range(len(crabs)):
    fuel += abs(crabs[i]-med)
print(med, int(fuel))
# 311, 347011
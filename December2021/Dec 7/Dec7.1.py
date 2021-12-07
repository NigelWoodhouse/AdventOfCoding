import statistics

f = open("numbers.txt", "r")
crabs = f.readline().split(",")
crabs = list(map(int, crabs))

# print(crabs)
# print(statistics.median(crabs))
med = statistics.median(crabs)
fuel = 0
for i in range(len(crabs)):
    fuel += abs(crabs[i]-med)
print(int(fuel))
# 347011
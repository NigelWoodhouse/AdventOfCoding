cycleNum = 0
count = 0
varX = 1
signalStrength = [20,60,100,140,180,220]

def incrementSignalStrength(cycleNum, count):
    cycleNum += 1
    if (cycleNum in signalStrength):
        count += cycleNum*varX
        print(cycleNum*varX, cycleNum, varX)
    return cycleNum, count

file = open("input.txt", "r")
for line in file:
    command = line.split(' ')
    if command[0] == "noop\n" or command[0] == "noop":
        cycleNum, count = incrementSignalStrength(cycleNum, count)
    else:
        cycleNum, count = incrementSignalStrength(cycleNum, count)
        varX += int(command[1])
        cycleNum, count = incrementSignalStrength(cycleNum, count)
print(count) 
# 15120
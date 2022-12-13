cycleNum = 0
count = 0
varX = 1
signalStrength = [20,60,100,140,180,220]

file = open("input.txt", "r")
for line in file:
    command = line.split(' ')
    if command[0] == "noop\n" or command[0] == "noop":
        cycleNum += 1
        print(cycleNum)
    else:
        cycleNum += 1
        if (cycleNum in signalStrength):
            count += cycleNum*varX
        varX += int(command[1])
        cycleNum += 1
        if cycleNum == -2:
            count += cycleNum*varX
print(count)
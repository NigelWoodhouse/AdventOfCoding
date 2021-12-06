import matplotlib.pyplot as plt
f = open("numbers.txt", "r")
fish = f.readline().split(",")
fish = list(map(int, fish))

fish_state = [0]*9
for i in range(len(fish_state)):
    fish_state[i] = fish.count(i)
print(fish_state)

count=[]

for day in range(1, 257):
    count.append(sum(fish_state))
    new_fish = fish_state[0]
    fish_state.pop(0)
    fish_state.append(0)
    fish_state[6] += new_fish
    fish_state[8] += new_fish
print(sum(fish_state))
# 1705008653296

plt.plot(range(1,257),count)
plt.title('Number of Swimmy Boys')
plt.xlabel('Day')
plt.ylabel('Fishy boys')
plt.savefig("FishCount.png", bbox_inches='tight', dpi=1000)
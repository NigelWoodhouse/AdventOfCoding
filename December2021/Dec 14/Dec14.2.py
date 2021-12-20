from collections import Counter
import json
base_polymer = "HBCHSNFFVOBNOFHFOBNO"
with open("pairinsertions2.json") as pair_insertions:
    pair_insertions = json.load(pair_insertions)
characters = Counter(base_polymer)
pairs_counter = {}

# Initiate all pairs
for entries in pair_insertions:
    pairs_counter[entries] = 0

# Set initial count for pairs
for l in range(len(base_polymer)-1):
    pairs_counter[base_polymer[l]+base_polymer[l+1]] += 1

# Iterate through 40 times
for count in range(40):
    for key, value in pairs_counter.copy().items(): # iterate through items in dictonary. Use .copy() so it doesnt change during the same iteration
        char = pair_insertions[key] # Get the new character from the pair
        pairs_counter[key] -= value # Remove the pair
        pairs_counter[key[0]+char] += value # Increase resultant new pair
        pairs_counter[char+key[1]] += value # Increase resultant new pair
        characters[char] += value # Increase the count of the character
        print(characters[char])
print(max(characters.values())-min(characters.values()))
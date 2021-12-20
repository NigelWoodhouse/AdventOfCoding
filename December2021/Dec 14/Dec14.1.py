import json
from collections import Counter

with open("pairinsertions.json") as pair_insertions:
    pair_insertions = json.load(pair_insertions)

def polymer(base_polymer):
    new_polymer = ""
    for i in range(len(base_polymer)-1):
        key = base_polymer[i]+base_polymer[i+1]
        new_polymer += pair_insertions[key]
    new_polymer += base_polymer[-1]
    return new_polymer

def calc_characters(base_polymer):
    char = Counter(base_polymer)
    max_char = max(char, key = char.get)
    max_char_count = base_polymer.count(max_char)
    min_char = min(char, key = char.get)
    min_char_count = base_polymer.count(min_char)
    
    
    return max_char, max_char_count, min_char, min_char_count

def main():
    base_polymer = "HBCHSNFFVOBNOFHFOBNO"
    for i in range(40):
        base_polymer = polymer(base_polymer)
        print(i)
    print(base_polymer)
    character_calculation = calc_characters(base_polymer)
    print(character_calculation, character_calculation[1]-character_calculation[3])
# 3408
main()
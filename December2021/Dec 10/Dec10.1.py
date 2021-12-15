f = open("numbers.txt", "r")
lines = f.read().split("\n")
print(lines)

sum = 0

# Python should have switch cases now???
for element in range(len(lines)):
    opening_array = []
    closing_array = []
    for char in lines[element]:
        if char == "(":
            closing_array.append(")")
        elif char == "[":
            closing_array.append("]")
        elif char == "{":
            closing_array.append("}")
        elif char == "<":
            closing_array.append(">")
        elif char == ")":
            if closing_array[-1] != ")":
                sum += 3
            closing_array = closing_array[:-1]
        elif char == "]":
            if closing_array[-1] != "]":
                sum += 57
            closing_array = closing_array[:-1]
        elif char == "}":
            if closing_array[-1] != "}":
                sum += 1197
            closing_array = closing_array[:-1]
        elif char == ">":
            if closing_array[-1] != ">":
                sum += 25137
            closing_array = closing_array[:-1]
print(sum)
# 299793
f = open("numbers.txt", "r")
lines = f.read().split("\n")

sum = 0

# Python should have switch cases now???
for element in range(len(lines)):
    opening_array = []
    closing_array = []
    for char in lines[element]:
        match char:
            case "(":
                closing_array.append(")")
            case "[":
                closing_array.append("]")
            case "{":
                closing_array.append("}")
            case "<":
                closing_array.append(">")
            case ")":
                if closing_array[-1] != ")":
                    sum += 3
                closing_array = closing_array[:-1]
            case "]":
                if closing_array[-1] != "]":
                    sum += 57
                closing_array = closing_array[:-1]
            case "}":
                if closing_array[-1] != "}":
                    sum += 1197
                closing_array = closing_array[:-1]
            case ">":
                if closing_array[-1] != ">":
                    sum += 25137
                closing_array = closing_array[:-1]
print(sum)
# 299793
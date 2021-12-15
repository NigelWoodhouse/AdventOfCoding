import statistics
f = open("numbers.txt", "r")
lines = f.read().split("\n")

sum = 0
sum_list=[]

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
    if sum != 0:
        sum = 0
    else:
        sum2 = 0
        closing_array.reverse()
        for chars in closing_array:
            if chars == ")":
                sum2 = sum2 * 5 + 1
            elif chars == "]":
                sum2 = sum2 * 5 + 2
            elif chars == "}":
                sum2 = sum2 * 5 + 3
            elif chars == ">":
                sum2 = sum2 * 5 + 4
        sum_list.append(sum2)
print(statistics.median(sum_list))
# 3654963618
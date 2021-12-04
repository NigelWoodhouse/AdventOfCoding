f = open('numbers.txt', 'r')
content = f.readlines()

num_numbers = len(content)
len_num = len(content[0])-1
print(num_numbers, len_num)

bin_array = [0]*len_num
gamma = ""
epsilon = ""

for i in range(num_numbers):
    for j in range(len_num):
        if content[i][j] == str(1):
            bin_array[j] += 1
print(bin_array)


for i in range(len(bin_array)):
    if bin_array[i] > num_numbers/2:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"
gamma = int(gamma,2)
epsilon = int(epsilon,2)
product = gamma*epsilon
print("Gamma: %i Epsilon: %i Product: %i " %(gamma, epsilon, product))
from operator import mod
from math import lcm
class Monkey(object):
    def __init__(self, items, operand, operation, divisor):
        self.items = items
        self.operand = operand
        self.operation = operation
        self.divisor = divisor
    
    def inspectMultiply(self, item):
        if self.operation != 0:
            self.items[item] *= self.operation
        else:
            self.items[item] *= self.items[item]
    
    def inspectAdd(self, item):
        if self.operation != 0:
            self.items[item] += self.operation
        else:
            self.items[item] += self.items[item]

    def sortItem(self, item, monkey_pass_true, monkey_pass_false):
        self.count += 1
        item = mod(item, lcm(*[2, 3, 5, 7, 11, 13, 17, 19])) # get remainder of lowest common multiple from primes. Chinese remainder theorem
        if item % self.divisor == 0:
            monkey_pass_true.items.append(item)
        else:
            monkey_pass_false.items.append(item)
        
if __name__ == '__main__':
    # Hardcoded test input
    # Monkey0 = Monkey([79, 98], "*", 19, 23)
    # Monkey1 = Monkey([54, 65, 75, 74], "+", 6, 19)
    # Monkey2 = Monkey([79, 60, 97], "*", 0, 13)
    # Monkey3 = Monkey([74], "+", 3, 17)

    # Monkey0.self_true, Monkey0.self_false, Monkey0.count = Monkey2, Monkey3, 0
    # Monkey1.self_true, Monkey1.self_false, Monkey1.count = Monkey2, Monkey0, 0
    # Monkey2.self_true, Monkey2.self_false, Monkey2.count = Monkey1, Monkey3, 0
    # Monkey3.self_true, Monkey3.self_false, Monkey3.count = Monkey0, Monkey1, 0

    # monkeys = [Monkey0, Monkey1, Monkey2, Monkey3]

    # Hardcoded input
    Monkey0 = Monkey([54, 89, 94], "*", 7, 17)
    Monkey1 = Monkey([66, 71], "+", 4, 3)
    Monkey2 = Monkey([76, 55, 80, 55, 55, 96, 78], "+", 2,  5)
    Monkey3 = Monkey([93, 69, 76, 66, 89, 54, 59, 94], "+", 7, 7)
    Monkey4 = Monkey([80, 54, 58, 75, 99], "*", 17, 11)
    Monkey5 = Monkey([69, 70, 85, 83], "+", 8, 19)
    Monkey6 = Monkey([89], "+", 6,  2)
    Monkey7 = Monkey([62, 80, 58, 57, 93, 56], "*", 0, 13)

    Monkey0.self_true, Monkey0.self_false, Monkey0.count = Monkey5, Monkey3, 0
    Monkey1.self_true, Monkey1.self_false, Monkey1.count = Monkey0, Monkey3, 0
    Monkey2.self_true, Monkey2.self_false, Monkey2.count = Monkey7, Monkey4, 0
    Monkey3.self_true, Monkey3.self_false, Monkey3.count = Monkey5, Monkey2, 0
    Monkey4.self_true, Monkey4.self_false, Monkey4.count = Monkey1, Monkey6, 0
    Monkey5.self_true, Monkey5.self_false, Monkey5.count = Monkey2, Monkey7, 0
    Monkey6.self_true, Monkey6.self_false, Monkey6.count = Monkey0, Monkey1, 0
    Monkey7.self_true, Monkey7.self_false, Monkey7.count = Monkey6, Monkey4, 0

    monkeys = [Monkey0, Monkey1, Monkey2, Monkey3, Monkey4, Monkey5, Monkey6, Monkey7]

    passes = []
    # one cycle
    for i in range(1,10001):
        for monkey in monkeys:
            for item in range(len(monkey.items)):
                if monkey.operand == "*":
                    monkey.inspectMultiply(item)
                elif monkey.operand == "+":
                    monkey.inspectAdd(item)
                monkey.sortItem(monkey.items[item], monkey.self_true, monkey.self_false)
            monkey.items = []
    for monkey in monkeys:
        passes.append(monkey.count)
    passes.sort(reverse=True)
    print(passes[0]*passes[1])       
# 25590400731
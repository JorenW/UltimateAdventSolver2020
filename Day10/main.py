class Adapter:
    outputvalue = None
    possibleSuccessors = []

    def __init__(self, pointer, numbers):
        
        self.outputvalue = numbers[pointer]
        successorpointers = self.find_successors(pointer, numbers)
        # print(successorpointers)
        self.possibleSuccessors = map(lambda x: Adapter(x, numbers), successorpointers)
        # print([x.outputvalue for x in possibleSuccessors])

    def find_successors(self, pointer, numbers):
        result = []
        pointer = pointer + 1
        while(numbers[pointer] - self.outputvalue <= 3 and pointer < len(numbers) - 1):
            result.append(pointer)
            pointer = pointer + 1
        return result


def part1(numbers):
    pointer = 1
    onecount = 0
    threecount = 0

    while(pointer < len(numbers)):
        diff = numbers[pointer] - numbers[pointer - 1]
        if(diff == 1):
            onecount = onecount + 1
        elif(diff == 3):
            threecount = threecount + 1

        pointer += 1
    print(onecount * threecount)

def bfs(tree, numbers):
    stack = [tree]
    result = 0
    while(len(stack) != 0):
        next = stack.pop()
        if(next.outputvalue == numbers[len(numbers) - 1]):
            result = result + 1
            print(result)
        
        for c in next.possibleSuccessors:
            stack.append(c)
    
    return result

def part2(numbers):
    print(numbers)
    print("building tree")
    tree = Adapter(0, numbers)
    print(map(lambda x: x.outputvalue, tree.possibleSuccessors))
    print("traversing tree")
    print(bfs(tree, numbers))


def find_precesoors(val, pointer, numbers):
        result = []
        pointer = pointer - 1
        while(val - numbers[pointer] <= 3 and pointer >= 0):
            result.append(pointer)
            pointer = pointer - 1
        return result


def part2dp(numbers):
    pointer = 1
    dp = [1]
    while(pointer < len(numbers)):
        result = find_precesoors(numbers[pointer], pointer, numbers)
        dp.append(sum(map(lambda a: dp[a], result)))
        pointer = pointer + 1
    
    return dp[len(dp) - 1]


if __name__ == "__main__":
    with open("input.txt") as f:
        numbers = [int(x) for x in f.read().split("\n")]
        numbers.append(0)
        numbers.append(max(numbers) + 3)
        print(part2dp(sorted(numbers)))
        
            

        

import math


def isValid(preamble, num):
    for p in preamble:
        if((num - p) in preamble):
            return True

def part1(numbers, prelength):
    
    pointer = prelength
    while(pointer < len(numbers)):
        if(not isValid(set(numbers[(pointer-prelength):pointer]), numbers[pointer])):
            return numbers[pointer]
        pointer = pointer + 1

def part2(numbers, invalidNum):
    
    startset = 0
    endset = 1
    sum = numbers[startset] + numbers[endset]
    
    while (sum != invalidNum):
        if(sum < invalidNum):
            endset = endset + 1
            sum = sum + numbers[endset]
        elif(sum > invalidNum):
            sum = sum - numbers[startset]
            startset = startset + 1
    
    return max(numbers[startset:endset+1]) + min(numbers[startset:endset+1]) 
    
            

if __name__ == "__main__":
    with open("input.txt") as f:
        numbers = [int(x) for x in f.read().split("\n")]
        invalidNum = part1(numbers, 25)
        print(part2(numbers, invalidNum))
        
            

        

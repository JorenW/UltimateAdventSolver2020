
def part1(numbers):
    p1, p2 = 0, 1

    while(numbers[p1] + numbers[p2] != 2020):
        if(p2 == len(numbers) -1):
            p1 += 1
            p2 = p1 + 1
        else:
            p2 += 1
    
    print(numbers[p1] * numbers[p2])

def part2(numbers):
    p1, p2, p3 = 0, 1, 2

    while(numbers[p1] + numbers[p2] + numbers[p3] != 2020):
        if(p3 == len(numbers) - 1):
            p2 += 1
            p3 = p2 + 1
        
        if(p2 == len(numbers) - 2):
            p1 += 1
            p2 = p1 + 1
        else:
            p3 += 1
    
    print(numbers[p1] * numbers[p2] * numbers[p3])

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
        numbers = map(lambda x: int(x), lines)

        part1(numbers)
        part2(numbers)
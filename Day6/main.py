import math

def group_to_count(group):
    return len(set(filter(lambda x: x != "\n", group)))

def part1(groups):
    print(sum(map(lambda x: group_to_count(x), groups)))

def part2(groups):
    count = 0
    for group in groups:
        persons = map(lambda x: set(x), group.split("\n"))
        count = count + len(reduce(lambda a,b: a.intersection(b), persons))
    print(count)


if __name__ == "__main__":
    with open("input.txt") as f:
        groups = f.read().split("\n\n")
        part1(groups)
        part2(groups)
        

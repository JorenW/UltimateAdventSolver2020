import math

class Bagpointer:

    amount = None
    key = None

    def __init__(self, amount, key):
        self.amount = amount
        self.key = key


def string_to_bagpointer(line):
    if("no other" in line):
        return Bagpointer(1, None)

    amount = int(line[1])
    key = (" ".join(line[2:].split(" ")[1:3])).strip()
    return Bagpointer(amount, key)

def add_bag_to_dict(line, dict):
    key = " ".join(line.split("contain")[0].split(" ")[0:2])
    values = map(lambda x: string_to_bagpointer(x), line.split("contain")[1].split(","))
    dict[key] = values
    return dict

def traverse_bag(bag, dict):
    stack = map(lambda x: x.key, list(dict[bag]))
    
    while(len(stack) != 0):
        b = stack.pop()
        
        if(b == None):
            continue
        
        for child in dict[b]:
            stack.append(child.key)

        if("shiny gold" == b):
            return True
        
        
    
    return False

def traverse_bag_count(bags, dict):
    if(bags[0].key == None):
        return 1
    
    result = 1
    for bag in bags:
        result = result + (bag.amount * traverse_bag_count(dict[bag.key], dict))

    return result


def part1(dict):
    colors = map(lambda x: traverse_bag(x, dict), dict.keys())
    print(colors.count(True))

def part2(dict):
    # -1, dont count the gold bag itself
    print(traverse_bag_count(dict["shiny gold"], dict) - 1)


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().split("\n")

        dict = {}
        for line in lines:
            add_bag_to_dict(line, dict)

        part2(dict)

        

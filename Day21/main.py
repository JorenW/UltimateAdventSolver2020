import copy
def get_allergens(lines):
    result = {}
    ing_result = []
    for line in lines:
        line = line.replace("(", "")
        line = line.replace(")", "")
        spl = line.split("contains")
        ingredients = spl[0].strip().split(" ")
        allergens = spl[1].strip().split(", ")
        ing_result = ing_result + (ingredients)
        for a in allergens:
            if a not in result:
                result[a] = copy.deepcopy(set(ingredients))
            else:
                result[a] = result[a].intersection(set(ingredients))

    return result, ing_result

def eliminate(allergens, val):
    for a in allergens:
        allergens[a] = allergens[a] - val

def print_result(result):
    pr = ""
    for k in sorted(result.keys()):
        pr = pr + "," + result[k].pop()
    
    print(pr[1:])

def part2(lines):
    allergens, ingredients = get_allergens(lines)
    print(allergens)
    result = {} 

    while(len(reduce(lambda a,b: a.union(b), allergens.values())) != 0):
        # print(result)
        # print(allergens)
        for a in allergens:
            vals = copy.deepcopy(allergens[a])
            if len(vals) == 1:
                result[a] = vals
                eliminate(allergens, vals)


    print_result(result)


    # print(",".join(sorted(map(lambda x: x.pop(), result.values()))))

def part1(lines):
    allergens, ingredients = get_allergens(lines)
    dangerous_ingredients = reduce(lambda a,b: a.union(b), allergens.values())
    safe_ingredients = map(lambda x: ingredients.count(x), set(ingredients) - dangerous_ingredients)
    print(sum(safe_ingredients))


if __name__ == "__main__":
    with open("input2.txt") as f:
        lines = f.read().split("\n")

        part2(lines)
        
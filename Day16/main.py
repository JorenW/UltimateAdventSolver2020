class R():

    min, max = 0,0
    def __init__(self, s):
        spl = s.split("-")
        self.min = int(spl[0])
        self.max = int(spl[1])


    def inRange(self, i):
        return i >= self.min and i <= self.max

    def __str__(self):
        return "[" + str(self.min)+","+str(self.max)+"]"

flatten = lambda t: [item for sublist in t for item in sublist]

def parse_range(s):
    return map(R, s.strip().split(" or "))

def setup(lines):
    rules = {}
    i = 0
    while(lines[i] != ""):
        spl = lines[i].split(":")
        rules[spl[0]] = parse_range(spl[1])
        i = i + 1

    i = i + 2
    my_ticket = [int(x) for x in lines[i].split(",")]

    i = i + 3
    nearby_tickets = []
    while(i < len(lines)):
        nearby_tickets.append([int(x) for x in lines[i].split(",")])
        i = i + 1

    return rules, my_ticket, nearby_tickets

def part1(lines):
    rules, my_ticket, nearby_tickets = setup(lines)
    flat_rules = flatten(rules.values())
    print([str(x) for x in flat_rules])

    print("Start checking")
    error_rate = 0
    for ticket in nearby_tickets:
        for n in ticket:
            if not any(map(lambda x: x.inRange(n), flat_rules)):
                error_rate = error_rate + n

    print(error_rate)


def part2(lines):
    rules, my_ticket, nearby_tickets = setup(lines)
    flat_rules = flatten(rules.values())
    
    # eliminate tickets
    new_tickets = []
    for ticket in nearby_tickets:
        valid = True
        for n in ticket:
            valid = valid and any(map(lambda x: x.inRange(n), flat_rules))
        
        if(valid):
            new_tickets.append(ticket)


    # find possible positions for all fields 
    my_fields = {}
    new_tickets.append(my_ticket)

    for field in rules.keys():
        pos = 0
        possible_positions = []
        
        while pos < len(my_ticket):
            isPos = True
            
            for t in new_tickets:
                isPos = isPos and reduce(lambda a,b: a != b, map(lambda x: x.inRange(t[pos]), rules[field]))
                if not isPos:
                    break

            if(isPos):
                possible_positions.append(pos)
                
            pos = pos + 1
        
        my_fields[field] = sorted(possible_positions)

    # solve by sweeping
    result = {}
    previous = None
    for a in sorted(my_fields, key=lambda x: len(my_fields[x])):
        if(len(my_fields[a]) == 1):
            result[a] = my_fields[a][0]
            previous = set(my_fields[a])
        else:
            result[a] = (set(my_fields[a]) - previous).pop()
            previous = set(my_fields[a])

    # find prod for all departure fields
    departure_keys = filter(lambda x: "departure" in x, my_fields.keys())
    prod = 1
    for k in departure_keys:
        prod = prod * my_ticket[result[k]]    
    print(prod)

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().split("\n")
        part2(lines)
        
            

        

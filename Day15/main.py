def expand_stringvalue(string_value, length):
    prepend = "0" * (length - (len(string_value)))
    return prepend + string_value

def string_to_stringvalue(val, length):
    val = str(bin(int(val))) #stringify
    return expand_stringvalue(val[2:], length) #strip 0b --> reverse --> inflate by prepend

def stringvalue_to_int(stringvalue):
    return int(stringvalue, 2)

def maskValue(mask, value):
    result = ""
    # print(string_value)

    for i in range(36):
        if(mask[i] == "X"):
            result = result + value[i]
        else:
            result = result + mask[i]

    return result

def part1(instructions):
    memory = {}
    mask = ""

    for i in instructions:
        spl = i.split(" = ")
        type = spl[0]
        val = spl[1]

        
        if(type == "mask"):
            mask = val
        else:
            address = type[4:-1]

            val = string_to_stringvalue(val)
            masked = maskValue(mask, val)
            
            # print(masked)
            # print(stringvalue_to_int(masked))
            memory[address] = stringvalue_to_int(masked)

    return sum(memory.values())


def possible_destinations(masked):
    xcount = masked.count("X")
    length = pow(2, masked.count("X"))
    i = 0
    results = []
    while i < length:
        res = ""
        bits = expand_stringvalue(str(bin(i))[2:], xcount)
        # print(bits)
        count = 0
        for b in masked:
            if(b == "X"):
                res = res + bits[count]
                count = count + 1
            else:
                res = res + b

        results.append(res)
        i = i + 1
    return results


def maskAdress(mask, address):
    masked = ""
    for i in range(36):

        if(mask[i] == "X"):
            masked = masked + "X"
        elif(mask[i] == "1"):
            masked = masked + "1"
        else:
            masked = masked + address[i]
    return masked


def part2(instructions):
    memory = {}
    mask = ""

    for i in instructions:
        spl = i.split(" = ")
        type = spl[0]
        val = spl[1]

        
        if(type == "mask"):
            mask = val
        else:
            address = type[4:-1]
            address_string = string_to_stringvalue(address, 36)
            # print(mask)
            # print(address_string)
            masked = maskAdress(mask, address_string)
            destinations = possible_destinations(masked)
            
            for dest in destinations:
                print(int(dest, 2))
                memory[dest] = int(val)

            # print(masked)
            # print(stringvalue_to_int(masked))
            # memory[address] = stringvalue_to_int(masked)
    
    return sum(memory.values())

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().split("\n")
        print(part2(lines))
        # num = 0b1101
        # print(num)
        
            

        

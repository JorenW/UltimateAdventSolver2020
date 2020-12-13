import copy
import functools

def part2(busids):
    t = 195312351877638043 - 1

    length = 0
    while(length != len(busids)):
        for id in busids:
            if id == "x":
                length = length + 1
            else:
                if (t + length) % int(id) == 0:
                    length = length + 1
                else:
                    length = 0
                    break
            print(t, length)
        t = t + 1
    print(length)

def part2_smart(busids):
    t = 0
    N = 1
    for ids in busids:
        if(ids == "x"):
            continue
        N = N * int(ids)
        

    for i in range(len(busids)):
        if(busids[i] == "x"):
            continue

        bi = i
        ni = int(busids[i])
        Ni = int(N / ni)
        # print(Ni)
        xi = pow(Ni, -1, ni)
        # print((Ni * xi) % ni)
        t = t + ((bi * Ni * xi))

    return  N - t % N
    


def part1(arrival, busses):
    original_busses = copy.deepcopy(busses)

    for i in range(len(busses)):
        while(busses[i] < arrival):
            busses[i] = busses[i] + original_busses[i]
        busses[i] = busses[i] - arrival

    busid = original_busses[busses.index(min(busses))]
    print(busid * min(busses))


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().split("\n")
        arrival = int(lines[0])
        busses = [int(x) for x in filter(lambda x: x != "x", lines[1].split(","))]
        # part1(arrival, busses)
        print(part2_smart(lines[1].split(",")))
        
            

        

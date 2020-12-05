import math

def binary_search(instructions, lowerbound, upperbound):
    for i in instructions:
        if i == 0:
            upperbound = upperbound - ((upperbound - lowerbound + 1) / 2)
        else:
            lowerbound = lowerbound + ((upperbound - lowerbound + 1) / 2)
    
    return upperbound

def seat_to_id((r,c)):
    return r * 8 + c

def seat_to_rc(seat):
    seat = filter(lambda x: x != "\n", seat)
    rowletters = map(lambda x: 0 if x == "F" else 1, seat[0:7])
    columnletters = map(lambda x: 0 if x == "L" else 1, seat[7:])
    
    row = binary_search(rowletters, 0, 127)
    column = binary_search(columnletters, 0, 7)
    
    return(row, column)

def part1(seats):
    seats = map(lambda x: seat_to_id(seat_to_rc(x)), seats)
    return max(seats)

def part2(seats):
    seats = set(map(lambda x: seat_to_id(seat_to_rc(x)), seats))

    for r in range(128):
        for c in range(8):
            id = seat_to_id((r,c))
            if id not in seats and id - 1 in seats and id + 1 in seats:
                return id
    

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()

        print(part1(lines))
        print(part2(lines))
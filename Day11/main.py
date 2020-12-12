import copy


def no_adjacent_seats_occupied(matrix, x, y):
    adjacents = get_adjacent_indices(x, y, matrix, ["L", "."])
    return all(adjacents.values())

def min_four_occupied(matrix, x, y):
    adjacents = get_adjacent_indices(x, y, matrix, ["#"], False)
    return adjacents.values().count(True) >= 4

def get_adjacent_indices(i, j, matrix, checks, default=True):
    up, down, left, right, leftup, leftdown, rightup, rightdown = False, False, False, False, False, False, False, False
    n = len(matrix)
    m = len(matrix[0])
    if i > 0:
        left = matrix[j][i-1] in checks
    else:
        left = default

    if i+1 < m:
        right = matrix[j][i + 1] in checks
    else:
        right = default

    if j > 0:
        up = matrix[j - 1][i] in checks
    else:
        up = default

    if j+1 < n:
        down = matrix[j+1][i] in checks
    else:
        down = default

    if i > 0 and j > 0:
        leftup = matrix[j-1][i-1] in checks
    else:
        leftup = default
    if i > 0 and j + 1 < n:
        leftdown = matrix[j+1][i - 1] in checks
    else:
        leftdown = default

    if i + 1 < m and j > 0:
        rightup = matrix[j - 1][i + 1] in checks
    else:
        rightup = default

    if i + 1 < m and j+1 < n:
        rightdown = matrix[j+1][i + 1] in checks
    else:
        rightdown = default


    return {"up": up, "down": down, "left": left, "right": right, "leftup": leftup, "leftdown": leftdown, "rightup": rightup, "rightdown": rightdown}

def inbound(n, min, max):
    return n >= 0 and n < max

def find_first_seat_in_dir(dirx, diry, x, y, matrix):
    result = None
    while(inbound(x + dirx, 0, len(matrix[0])) and inbound(y + diry, 0, len(matrix)) and result == None):
        x = x + dirx
        y = y + diry
        if matrix[y][x] != ".":
            result = matrix[y][x]
    
    return result

def five_occupied(matrix, x, y):
    dirs = [-1,0, 1]
    count = 0
    for dirx in dirs:
        for diry in dirs:
            if(dirx == 0 and diry == 0): 
                continue
            if(find_first_seat_in_dir(dirx, diry, x, y, matrix) == "#"):
                count = count + 1
    
    return count >= 5

def no_adjacent_seats_occupied2(matrix, x, y):
    dirs = [-1,0, 1]
    count = 0
    for dirx in dirs:
        for diry in dirs:
            if(dirx == 0 and diry == 0): 
                continue
            if(find_first_seat_in_dir(dirx, diry, x, y, matrix) != "#"):
                count = count + 1
    
    return count == 8

def manipulate_matrix(matrix):
    next = []
    for y in range(len(matrix)):
        row = []
        for x in range(len(matrix[0])):
            # print(matrix[y])
            s = matrix[y][x]
            if(s == "L" and no_adjacent_seats_occupied2(matrix, x, y)):
                row.append("#")
            elif(s == "#" and five_occupied(matrix, x, y)):
                row.append("L")
            else:
                row.append(s)
        next.append(row)

    return next

def pretty_print(matrix):
    print("\n".join(["".join(x) for x in matrix]))

def count_occupied(matrix):
    m = [("".join(x)).count("#") for x in matrix]
    return sum(m)

def part1(matrix):
    next = manipulate_matrix(matrix)
    pretty_print(next)
    count = 1

    while(next != matrix):
        print("STEP ------------------ " + str(count))
        matrix = next
        next = manipulate_matrix(next)
        pretty_print(next)
        count = count + 1

        # if(count == 2):
        #     break
    print(count_occupied(matrix))

    # print(next)


    


if __name__ == "__main__":
    with open("input.txt") as f:
        matrix = [list(x) for x in f.read().split("\n")]
        # print(matrix)
        part1(matrix)
        # print(get_adjacent_indices(7,6, matrix, "L"))
            

        

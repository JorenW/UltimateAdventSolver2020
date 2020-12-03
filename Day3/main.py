import vector as v



def part1(rows, operation):
    width = len(rows[0]) - 1

    pos = v.Vector2D(0, 0)
    treecount = 0

    while(pos.y != len(rows) - 1):
        pos = pos + operation
        pos.x = pos.x % width
        if(rows[pos.y][pos.x] == "#"):
            treecount += 1

    return treecount
    
def part2(rows):
    slope1 = part1(rows, v.Vector2D(1,1))
    slope2 = part1(rows, v.Vector2D(3,1))
    slope3 = part1(rows, v.Vector2D(5,1))
    slope4 = part1(rows, v.Vector2D(7,1))
    slope5 = part1(rows, v.Vector2D(1,2))
    
    return slope1 * slope2 * slope3 * slope4 * slope5

if __name__ == "__main__":
    with open("input.txt") as f:
        rows = f.readlines()
        
        print(part1(rows, v.Vector2D(3,1)))
        print(part2(rows))
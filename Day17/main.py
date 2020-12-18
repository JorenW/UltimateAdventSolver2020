import numpy as np
import copy

class Grid():
    # indexing by [z,y,x]
    gridlength = 51
    transform = int(gridlength/2) + 1
    array = np.zeros([gridlength, gridlength, gridlength, gridlength])

    def __init__(self, lines, array = None):
        if(array != None):
            self.array = copy.deepcopy(array)
            return

        y = 0
        for row in lines:
            x = 0
            for el in row:
                if el == "#":
                    self.set((x,y,0,0), 1)
                x = x + 1
            y = y + 1
            

    def getAllActive(self):
        result = []
        for x in range(self.gridlength):
            for y in range(self.gridlength):
                for z in range(self.gridlength):
                    for w in range(self.gridlength):
                        if(self.array[z,y,x,w] == 1):
                            result.append((x - self.transform, y - self.transform, z - self.transform, w - self.transform))
        
        return result

    def getAllCoords(self):
        result = []
        t = range(self.gridlength)[1:self.gridlength - 1]
        for x in t:
            for y in t:
                for z in t:
                    for w in t:
                        result.append((x - self.transform, y - self.transform, z - self.transform, w - self.transform))
        
        return result


    def get(self, (x,y,z,w)):
        return self.array[z + self.transform,y + self.transform,x + self.transform, w + self.transform]

    def set(self, (x,y,z,w), value):
        self.array[z + self.transform,y + self.transform,x + self.transform, w + self.transform] = value

    def getneighbours(self, (x, y, z,w)):
        options = [-1, 0, 1]
        result = []
        for a in options:
            for b in options:
                for c in options:
                    for d in options:
                        if (a == 0 and b == 0 and c == 0 and d == 0):
                            continue
                    result.append((x + a, y + b, z + c, w + d))
                    # print((x + a, y + b, z + c))

        return result

    def copy(self):
        return copy.deepcopy(self)

    def get_z_slice(self, z):
        return self.array[z + self.transform,:,:,:]

def part1(lines):
    grid = Grid(lines)
    
    for i in range(6):
        newGrid = Grid(lines, grid.array)
        # print(newGrid.get_z_slice(0))
        # newGrid.array = copy.deepcopy(grid.array)
        print("Round " + str(i))

        for coords in grid.getAllCoords():
            neighbours = grid.getneighbours(coords)
            
            s = map(lambda x: grid.get(x), neighbours)
            if grid.get(coords) == 1:
                # print(sum(s), coords)
                # return
                if sum(s) == 2 or sum(s) == 3:
                    newGrid.set(coords, 1)
                else:
                    newGrid.set(coords, 0)
            else:
                if sum(s) == 3:
                    newGrid.set(coords, 1)
                else:
                    newGrid.set(coords, 0)
        
        grid = newGrid
        


    activeCount = sum(map(lambda x: grid.get(x), grid.getAllActive()))
    print(activeCount)            
    # for activecoords in grid.getAllActive

    return


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().split("\n")
        part1(lines)
        
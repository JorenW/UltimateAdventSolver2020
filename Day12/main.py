import math

class Waypoint:
    posx, posy = 10,1

    def rotate(self, degrees):
        degrees = math.radians(degrees)
        cs = math.cos(degrees)
        sn = math.sin(degrees)
        newx = self.posx * cs - self.posy * sn
        newy = self.posx * sn + self.posy * cs
        self.posx = round(newx)
        self.posy = round(newy)

    def move(self, direction, amount):
        if(direction == "N"):
            self.posy = self.posy + amount
        elif(direction == "E"):
            self.posx = self.posx + amount
        elif direction == "W":
            self.posx = self.posx - amount 
        else:
            self.posy = self.posy - amount    
        print(self.posx, self.posy)


class Ship:
    rotation = 0
    posx, posy = 0,0
    direction = "E"
    w = Waypoint()


    def __init__(self, instructions):
        for i in instructions:
            self.do_instruction(i[0], int(i[1:]))
        

    def do_instruction(self, i, amount):
        if(i == "N" or i == "W" or i == "S" or i == "E"):
            self.w.move(i, amount)
        elif(i == "L"):
            self.w.rotate(amount)
        elif(i == "R"):
            self.w.rotate(-amount)
        elif(i == "F"):
            dx = self.w.posx * amount
            dy = self.w.posy * amount
            self.posx = self.posx + dx
            self.posy = self.posy + dy
            print(self.posx, self.posy)

    def get_direction(self, degrees):
        degrees = degrees % 360
        if(degrees == 0):
            return "E"
        elif(degrees == 90):
            return "N"
        elif(degrees == 180):
            return "W"
        else:
            return "S"

    def move(self, direction, amount):
        
        if(direction == "N"):
            self.posy = self.posy + amount
        elif(direction == "E"):
            self.posx = self.posx + amount
        elif direction == "W":
            self.posx = self.posx - amount 
        else:
            self.posy = self.posy - amount    
        print(self.posx, self.posy)



def part1(lines):
    s = Ship(lines)
    print(abs(s.posy) + abs(s.posx))

def part2(lines):
    s = Ship(lines)
    print(abs(s.posy) + abs(s.posx))

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().split("\n")
        part2(lines)
        
            

        

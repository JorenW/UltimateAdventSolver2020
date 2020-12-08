import math

class Instruction:

    operation = None
    argument = None
    visited = False
    visitcount = 0

    def __init__(self, operation, argument):
        self.operation = operation
        self.argument = argument

    def flip(self):
        if(self.operation == "jmp"):
            self.operation = "nop"
        elif(self.operation == "nop"):
            self.operation = "jmp"

    def reset(self):
        self.visitcount = 0
        self.visited = False


def line_to_instruction(line):
    spl = line.split(" ")
    return Instruction(spl[0], int(spl[1]))

def part2(instructions):
    instructions = list(instructions)
    for i in instructions:
        i.reset()
    # print(map(lambda x: x.visitcount, instructions))

    pointer = 0
    acc = 0
    while(pointer != len(instructions)):
        i = instructions[pointer]
        if(i.visitcount == 100):
            return -1
            break


        if(i.operation == "jmp"):
            i.visitcount = i.visitcount + 1
            pointer = pointer + i.argument
        elif(i.operation == "acc"):
            i.visitcount = i.visitcount + 1
            acc = acc + i.argument
            pointer = pointer + 1
        elif(i.operation == "nop"):
            i.visitcount = i.visitcount + 1
            pointer = pointer + 1
    return acc



def part1(lines):
    instructions = map(lambda x: line_to_instruction(x), lines)

    pointer = 0
    acc = 0
    while(instructions[pointer].visited == False):
        i = instructions[pointer]
        if(i.operation == "jmp"):
            i.visited = True
            pointer = pointer + i.argument
        elif(i.operation == "acc"):
            i.visited = True
            acc = acc + i.argument
            pointer = pointer + 1
        elif(i.operation == "nop"):
            i.visited = True
            pointer = pointer + 1

        
    print(acc)

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().split("\n")
        instructions = map(lambda x: line_to_instruction(x), lines)

        for i in instructions:
            if(i.operation == "jmp" or i.operation == "nop"):
                i.flip()
                result = part2(instructions)
                if(result != -1):
                    print(result)
                i.flip()
            

        

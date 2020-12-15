class Memory():

    count, turn, turnbefore = 0, 0, 0
    def __init__(self, count, turn):
        self.count = count
        self.turn = turn


    def updateTurn(self, newTurn):
        self.turnbefore = self.turn
        self.turn = newTurn

def part1(numbers):
    
    dict = {}
    lastnum = None
    #Setup
    for num,i in zip(numbers, range(len(numbers))):
        dict[num] = Memory(1,i + 1)
        lastnum = num


    i = len(numbers) + 1
    while(i <= 30000000):
        mem = dict[lastnum]
        if(mem.count == 1):
            newnum = 0 
        else:
            newnum = mem.turn - mem.turnbefore

        if newnum not in dict:
            dict[newnum] = Memory(1, i)
        else:
            dict[newnum].updateTurn(i)
            dict[newnum].count = dict[newnum].count + 1

        lastnum = newnum
        i = i + 1
        
    print(lastnum)


if __name__ == "__main__":
    with open("input.txt") as f:
        numbers = [int(x) for x in f.read().split("\n")[0].split(",")]
        part1(numbers)
        # num = 0b1101
        # print(num)
        # print(zip(numbers))
        
            

        

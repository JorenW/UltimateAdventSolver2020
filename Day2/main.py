class PolicyPass:
    password = None
    policy_max = None
    policy_min = None
    policy_letter = None

    def __init__(self, line):
        parts = line.split(":")
        self.password = parts[1]
        self.policy_min = int(parts[0].split("-")[0])
        self.policy_max = int(parts[0].split("-")[1].split(" ")[0])
        self.policy_letter = parts[0].split("-")[1].split(" ")[1]

    def isValid(self):
        return (self.password[self.policy_min] == self.policy_letter) != (self.password[self.policy_max] == self.policy_letter)
        

def part1(lines):
    parsedlines = map(lambda x: PolicyPass(x).isValid(), lines)
    print(parsedlines.count(True))


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
        
        part1(lines)
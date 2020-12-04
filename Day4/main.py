import re

def isValidPass2(passport):
    byr = "byr" in passport and int(passport["byr"]) >= 1920 and int(passport["byr"]) <= 2002 
    iyr = "iyr" in passport and int(passport["iyr"]) >= 2010 and int(passport["iyr"]) <= 2020 
    eyr = "eyr" in passport and int(passport["eyr"]) >= 2020 and int(passport["eyr"]) <= 2030 
    
    hgtcm = "hgt" in passport and "cm" in passport["hgt"] and int(passport["hgt"][0:-2]) >= 150 and int(passport["hgt"][0:-2]) <= 193 
    hgtin = "hgt" in passport and "in" in passport["hgt"] and int(passport["hgt"][0:-2]) >= 59 and int(passport["hgt"][0:-2]) <= 76
    hgt = hgtcm or hgtin 

    hcl = "hcl" in passport and re.match("\#[\d|a|b|c|d|e|f]{6}", passport["hcl"]) != None and len(passport["hcl"]) == 7
    ecl = "ecl" in passport and passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    pid = "pid" in passport and re.match("\d{9}", passport["pid"]) != None and len(passport["pid"]) == 9
    return byr and iyr and eyr and hgt and hcl and ecl and pid
    # return pid

def isValidPass(passport):
    return "byr" in passport and "iyr" in passport and "eyr" in passport and "hgt" in passport and "hcl" in passport and "ecl" in passport and "pid" in passport

def insertinpass(currentpass, keyvaluesarray):
    print(keyvaluesarray)
    for keyvalue in keyvaluesarray:
        currentpass[keyvalue[0]] = keyvalue[1]
    return currentpass


def getkeyvalues(str):
    str = filter(lambda x: x != "\n", str)
    result = str.split(" ")
    return map(lambda x: x.split(":"), result)

def part1(lines):
    passports = []
    currentpass = {}
    for l in lines:
        if l == "\n":
            passports.append(currentpass)
            currentpass = {}
            continue

        currentpass = insertinpass(currentpass, getkeyvalues(l))
    passports.append(currentpass)
    passports = map(lambda x: isValidPass2(x), passports)    
    
    print(passports.count(True))

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
        
        part1(lines)
with open("C:/Users/Sam/Documents/AoC-2022/Day_1/input.txt", 'r') as inp:
    data = [i for i in inp.read().strip().split("\n")]

# part 1
curTotal = 0
curMax = 0
topElf = 0
secondElf = 0
thirdElf = 0
for i in range(len(data)):
    if data[i] != "":
        current = data[i]
        curTotal = curTotal + int(current)
    elif data[i] == "":
        if curMax < curTotal:
            curMax = curTotal
            curTotal = 0
        else: 
            curTotal = 0
        
    #checking elf scores
    if curMax > topElf:
        thirdElf = secondElf
        secondElf = topElf
        topElf = curMax
    elif curMax > secondElf:
        thirdElf = secondElf
        secondElf = curMax
    elif curMax > thirdElf:
        thirdElf = curMax


print(curMax)
print("top", topElf)
print("second", secondElf)
print("thid", thirdElf)
sumMax = topElf + secondElf + thirdElf
print(sumMax)
inp.close()


lineCounter = 0
matchCounter = 0;
with open("C:/Users/Sam/Documents/AoC-2022/Day_4/input.txt", 'r') as inp:
    curLine = inp.readline()
    while curLine:
        print(curLine)
        counter = counter + 1
        curLine = inp.readline()

print("lineCounter: " + lineCounter)
print("matchCounter: " + matchCounter)
inp.close()
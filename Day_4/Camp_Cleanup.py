
# lineCounter = 0
# matchCounter = 0
# with open("C:/Users/Sam/Documents/AoC-2022/Day_4/input.txt", 'r') as inp:
#     curLine = inp.readline()
#     while curLine:
#         # print(curLine)
#         lineCounter = lineCounter + 1
#         # splitting apart the current line into job a and b, then splitting a and b into start/end
#         a, b = curLine.split(',')
#         aStart, aEnd = a.split('-')
#         bStart, bEnd = b.split('-')
#         if aStart >= bStart and aEnd <= bEnd:
#             # print("aStart: ", aStart, "bStart: ", bStart)
#             matchCounter = matchCounter + 1

#         elif bStart >= aStart and bEnd <= aEnd:
#             # print("bStart: ", bStart, "aStart: ", aStart)
#             matchCounter = matchCounter + 1

#         curLine = inp.readline()

# print("lineCounter: ", lineCounter)
# print("matchCounter: ", matchCounter)
# inp.close()

with open("C:/Users/Sam/Documents/AoC-2022/Day_4/input.txt") as file:
    data = [i for i in file.read().strip().split("\n")]


# === PART 1 ===
pairs = 0
for entry in data:
    first, second = entry.split(",")
    first = [int(i) for i in first.split("-")]
    second = [int(i) for i in second.split("-")]

    if first[0] <= second[0] and first[1] >= second[1]:
        pairs += 1
    elif second[0] <= first[0] and second[1] >= first[1]:
        pairs += 1

print("Answer to part 1:", pairs)

# === PART 2 ===
pairs = 0
for entry in data:
    first, second = entry.split(",")
    first = [int(i) for i in first.split("-")]
    second = [int(i) for i in second.split("-")]

    if first[0] in range(second[0], second[1]+1) or first[1] in range(second[0], second[1]+1):
        pairs += 1
    elif second[0] in range(first[0], first[1]+1) or second[1] in range(first[0], first[1]+1):
        pairs += 1


print("Answer to part 2:", pairs)
import os, math, random, msvcrt

# row = [0, 0, 127, 0]
# row = [2, 0, 127, 0]
row = [0, 2, 127, 0]
# row = [0, 127, 4, 16]
# row = [127, 0, 4, 4]
# row = [0, 0, 0, 127]
# row = [127, 127, 0, 4]

splitRow = [[]]
obstacles = {}
n=0
for i in range(1,4): # check each value in row
    if row[i] == 0: # skip over 0s
        continue
    elif math.ceil(math.log2(row[i])) != math.floor(math.log2(row[i])): # check if value != 2^x aka obstacle
        n+=1
        obstacles[i]=row[i]
        splitRow.append([])
        continue
    splitRow[n].append(row[i])

output = []
tileCount = 0
i=0
while True:
    if splitRow[i] != []:
        for j in splitRow[i]:
            output.append(j)
            tileCount += 1
    i+=1
    if i == len(splitRow):
        break
    spaces = next(iter(obstacles))
    for j in range(spaces-tileCount): output.append(0)
    output.append(obstacles[spaces])

for k in range(4-len(output)): output.append(0)

print(output)
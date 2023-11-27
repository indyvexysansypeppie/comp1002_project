import os, math, random, msvcrt

# row = [0, 0, 127, 0]
# row = [2, 0, 127, 0]
# row = [0, 2, 127, 0]
# row = [0, 127, 4, 4]
# row = [127, 0, 4, 4]
# row = [0, 2, 2, 127]
row = [127, 4, 127, 4]

splitRow = [[]]
obstacles = {}
n=0
for i in range(4): # check each value in row
    if row[i] == 0: # skip over 0s
        continue
    elif math.ceil(math.log2(row[i])) != math.floor(math.log2(row[i])): # check if value != 2^x aka obstacle
        n+=1
        obstacles[i]=row[i]
        # print(obstacles)
        splitRow.append([])
        continue
    splitRow[n].append(row[i])

# print(splitRow)

output = []
i=0
while True:
    tileCount = 0 # count no of tiles in that split list
    if splitRow[i] != []: # empty lists are discarded
        for j in splitRow[i]:

            # sliding
            output.append(j)
            tileCount += 1
            
            # merging
            if (tileCount >= 2) and (output[-1] == output[-2]): # if there are >2 tiles and both tiles are same value
                output[-2] *= 2
                output[-1] = 0
                tileCount-1
    i+=1
    if i == len(splitRow):
        break
    spaces = next(iter(obstacles))
    for j in range(spaces-tileCount): output.append(0)
    output.append(obstacles[spaces])

for k in range(4-len(output)): output.append(0)

print(output)
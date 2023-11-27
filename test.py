import os, math, random, msvcrt

# row = [0, 0, 127, 0]
# row = [2, 0, 127, 0]
# row = [0, 2, 127, 0]
# row = [0, 127, 4, 4]
# row = [127, 0, 4, 4]
# row = [0, 2, 2, 127]
# row = [127, 0, 127, 4]
row = [127, 2, 2, 31]

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

outputRow = []
i=0
while True:
    tileCount = 0 # count no of tiles in that split list
    if splitRow[i] != []: # empty lists are discarded
        for j in splitRow[i]:

            # sliding
            outputRow.append(j)
            tileCount += 1
            
            # merging
            # should also increase score & break obstacle here
            if (tileCount >= 2) and (outputRow[-1] == outputRow[-2]): # if there are >2 tiles and both tiles are same value
                outputRow[-2] *= 2
                outputRow[-1] = 0
                tileCount-1
    i+=1
    if i == len(splitRow):
        break
    # spaces = next(iter(obstacles)) # retrieve index of obstacle
    # for j in range(spaces-tileCount): outputRow.append(0)
    # outputRow.append(obstacles[spaces])

    obsIDs = list(obstacles.keys()) # get list of the obstacles' indexes
    for j in range(obsIDs[i-1]-len(outputRow)): outputRow.append(0) # fill in empty spaces between tile & obstacles
    outputRow.append(obstacles[obsIDs[i-1]])

for k in range(4-len(outputRow)): outputRow.append(0)

print(outputRow)
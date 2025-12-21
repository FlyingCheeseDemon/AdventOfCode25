ranges = []

with open("input02.txt") as f:
    for line in f:
        ranges = line[:-1].split(",")

for i in range(len(ranges)):
    ranges[i] = ranges[i].split("-")
    for j in range(2):
        ranges[i][j] = int(ranges[i][j])

for ran in ranges:
    for id in range(ran[0],ran[1]+1):
        pass
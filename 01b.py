
dial_position = 50
password = 0

with open("input01.txt") as f:
    for line in f:
        direction = line[0]
        amount = int(line[1:-1])

        for i in range(amount):
            dial_position += (1 if direction == "R" else -1)
            if dial_position%100 == 0:
                password += 1

print(password)
with open("input.txt") as f:
    rows = [line.strip() for line in f]

safe = [i for i in range (0,100) ]

pwd = 0

curr = index = 50


for i in rows:
    rotation = i[0]
    if rotation == 'L':
        index = (index - int(i[1:])) % len(safe)
        curr = safe[index]
    if rotation == 'R':
        index = (index + int(i[1:])) % len(safe)
        curr = safe[index]
    if curr == 0:
        pwd += 1


print(pwd)